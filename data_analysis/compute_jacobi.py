# !/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (C) <2019-2021>  <Tamás Zolnai>  <zolnaitamas2000@gmail.com>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import pandas
import copy
import analyizer
import numpy
from utils import strToFloat, floatToStr, calcRMS

def computeHighFrequencies(jacobi_output_path, sequence):
    data_table = pandas.read_csv(jacobi_output_path, sep='\t')

    response_column = data_table["response"]
    trial_column = data_table["trial"]
    test_type_column = data_table["test_type"]

    tested_sequence = sequence
    tested_sequence += sequence[0]

    inclusion_high_count = 0
    exclusion_high_count = 0
    for i in range(len(trial_column)):
        if int(trial_column[i]) > 2:
            assert(i > 1)
            if (str(response_column[i - 2]) + str(response_column[i])) in tested_sequence:
                if test_type_column[i] == 'inclusion':
                    inclusion_high_count += 1
                else:
                    assert(test_type_column[i] == 'exclusion')
                    exclusion_high_count += 1
                
    
    return inclusion_high_count, exclusion_high_count

def computePalindromeFrequencies(jacobi_output_path):
    data_table = pandas.read_csv(jacobi_output_path, sep='\t')

    response_column = data_table["response"]
    trial_column = data_table["trial"]
    test_type_column = data_table["test_type"]

    inclusion_palindrome_count = 0
    exclusion_palindrome_count = 0
    for i in range(len(trial_column)):
        if int(trial_column[i]) > 2:
            assert(i > 1)
            if str(response_column[i - 2]) == str(response_column[i]):
                if test_type_column[i] == 'inclusion':
                    inclusion_palindrome_count += 1
                else:
                    assert(test_type_column[i] == 'exclusion')
                    exclusion_palindrome_count += 1
                
    
    return inclusion_palindrome_count, exclusion_palindrome_count

def computeJacobiTestData(input_dir, output_file):
    jacobi_data = pandas.DataFrame(columns=['subject', 'inclusion_high_ratio', 'exclusion_high_ratio',
                                                       'inclusion_high_ratio_without_palindromes', 'exclusion_high_ratio_without_palindromes'])

    for root, dirs, files in os.walk(input_dir):
        for subject in dirs:
            if subject.startswith('.'):
                continue

            print("Compute jacobi data for subject: " + str(subject))

            jacobi_output_path = os.path.join(root, subject, 'subject_' + subject + '__jacobi_log.txt')

            data_table = pandas.read_csv(jacobi_output_path, sep='\t')
            learning_sequence = str(data_table["PCode"][0])
            inclusion_high_count, exclusion_high_count = computeHighFrequencies(jacobi_output_path, learning_sequence)

            inclusion_palindrome_count, exclusion_palindrome_count = computePalindromeFrequencies(jacobi_output_path)

            all_triplet_count = 88
            jacobi_data.loc[len(jacobi_data)] = [subject, floatToStr(inclusion_high_count / all_triplet_count * 100),
                                                          floatToStr(exclusion_high_count / all_triplet_count * 100),
                                                          floatToStr(inclusion_high_count / (all_triplet_count - inclusion_palindrome_count) * 100),
                                                          floatToStr(exclusion_high_count / (all_triplet_count - exclusion_palindrome_count) * 100)]

        break

    jacobi_data.to_csv(output_file, sep='\t', index=False)

def computeFilterCriteria(jacobi_output_path):
    data_table = pandas.read_csv(jacobi_output_path, sep='\t')

    stimulus_column = data_table["response"]
    test_type_column = data_table["test_type"]
    run_column = data_table["run"]

    responses_8_inclusion = {}
    responses_8_exclusion = {}

    for i in range(0, len(stimulus_column), 8):
        count_1 = 0
        count_2 = 0
        count_3 = 0
        count_4 = 0
        ref_count = 2

        for j in range(i, i + 8):
            if str(stimulus_column[j]) == "1":
                count_1 += 1
            elif str(stimulus_column[j]) == "2":
                count_2 += 1
            elif str(stimulus_column[j]) == "3":
                count_3 += 1
            elif str(stimulus_column[j]) == "4":
                count_4 += 1

        diffs = [abs(ref_count - count_1)]
        diffs.append(abs(ref_count - count_2))
        diffs.append(abs(ref_count - count_3))
        diffs.append(abs(ref_count - count_4))
        rms = calcRMS(diffs)

        run = run_column[i]
        if test_type_column[i] == 'inclusion':
            if run not in responses_8_inclusion.keys():
                responses_8_inclusion[run] = [rms]
            else:
                responses_8_inclusion[run].append(rms)
        else:
            assert(test_type_column[i] == 'exclusion')
            if run not in responses_8_exclusion.keys():
                responses_8_exclusion[run] = [rms]
            else:
                responses_8_exclusion[run].append(rms)

    inclusion_filter = []
    for run in responses_8_inclusion.keys():
        inclusion_filter.append(floatToStr(sum(responses_8_inclusion[run])))

    exclusion_filter = []
    for run in responses_8_exclusion.keys():
        exclusion_filter.append(floatToStr(sum(responses_8_exclusion[run])))


    return inclusion_filter, exclusion_filter

def computeJacobiFilterCriteria(input_dir, output_file):
    jacobi_data = pandas.DataFrame(columns=['run', 'filter_criteria'])
    for root, dirs, files in os.walk(input_dir):
        for subject in dirs:
            if subject.startswith('.'):
                continue

            print("Compute jacobi filter data for subject: " + str(subject))

            jacobi_output_path = os.path.join(root, subject, 'subject_' + subject + '__jacobi_log.txt')
            filter_criteria_inclusion, filter_criteria_exclusion = computeFilterCriteria(jacobi_output_path)
            for i in range(1,5):
                run = "subject_" + subject + "_inclusion_" + str(i)
                jacobi_data.loc[len(jacobi_data)] = run, filter_criteria_inclusion[i - 1]
            for i in range(1,5):
                run = "subject_" + subject + "_exclusion_" + str(i)
                jacobi_data.loc[len(jacobi_data)] = run, filter_criteria_exclusion[i - 1]

        break

    jacobi_data.to_csv(output_file, sep='\t', index=False)
