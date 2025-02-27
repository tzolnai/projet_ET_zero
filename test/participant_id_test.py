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

import sys
import os
# Add the local path to the main script and external scripts so we can import them.
sys.path = [".."] + \
    [os.path.join("..", "externals", "psychopy_mock")] + sys.path

import unittest
import asrt
import shutil
import psychopy_gui_mock as pgm


class participantIDTest(unittest.TestCase):

    def tearDown(self):
        tempdir = os.path.abspath(__file__)
        (tempdir, trail) = os.path.split(tempdir)
        tempdir = os.path.join(tempdir, "data", "participant_id")

        # remove all temp files
        for file in os.listdir(tempdir):
            file_path = os.path.join(tempdir, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    def constructFilePath(self, file_name):
        filepath = os.path.abspath(__file__)
        (filepath, trail) = os.path.split(filepath)
        filepath = os.path.join(filepath, "data", "participant_id", file_name)
        return filepath

    def testNoSettingsFile(self):
        gui_mock = pgm.PsychoPyGuiMock()
        gui_mock.addFieldValues(
            [10, 'kontrol', 'férfi', 25, '3rd', '2nd'])

        thispath = self.constructFilePath("NoSettingsFile")
        experiment = asrt.Experiment(thispath)
        experiment.settings = asrt.ExperimentSettings("", "")
        experiment.settings.groups = ["kontrol", "exp1"]
        experiment.settings.numsessions = 2
        experiment.settings.epochN = 2
        experiment.settings.epochs = [1, 1]
        experiment.settings.block_in_epochN = 2
        experiment.settings.blockprepN = 5
        experiment.settings.blocklengthN = 20
        experiment.settings.asrt_rcolor = "Orange"
        experiment.settings.asrt_pcolor = "Green"
        experiment.settings.asrt_types = {}
        experiment.settings.asrt_types[1] = "implicit"
        experiment.settings.asrt_types[2] = "implicit"

        asrt.ensure_dir(os.path.join(thispath, "subject_settings"))

        experiment.participant_id()

        self.assertEqual(experiment.subject_group, 'kontrol')
        self.assertEqual(experiment.subject_number, 10)
        self.assertEqual(experiment.PCodes, {1: '3rd - 1324', 2: '2nd - 1243'})
        self.assertEqual(experiment.stim_output_line, 0)
        self.assertEqual(experiment.stim_sessionN, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1,
                                                    49: 1, 50: 1, 51: 2, 52: 2, 53: 2, 54: 2, 55: 2, 56: 2, 57: 2, 58: 2, 59: 2, 60: 2, 61: 2, 62: 2, 63: 2, 64: 2, 65: 2, 66: 2, 67: 2, 68: 2, 69: 2, 70: 2, 71: 2, 72: 2, 73: 2, 74: 2, 75: 2, 76: 2, 77: 2, 78: 2, 79: 2, 80: 2, 81: 2, 82: 2, 83: 2, 84: 2, 85: 2, 86: 2, 87: 2, 88: 2, 89: 2, 90: 2, 91: 2, 92: 2, 93: 2, 94: 2, 95: 2, 96: 2, 97: 2, 98: 2, 99: 2, 100: 2})
        self.assertEqual(experiment.stimepoch, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1,
                                                49: 1, 50: 1, 51: 2, 52: 2, 53: 2, 54: 2, 55: 2, 56: 2, 57: 2, 58: 2, 59: 2, 60: 2, 61: 2, 62: 2, 63: 2, 64: 2, 65: 2, 66: 2, 67: 2, 68: 2, 69: 2, 70: 2, 71: 2, 72: 2, 73: 2, 74: 2, 75: 2, 76: 2, 77: 2, 78: 2, 79: 2, 80: 2, 81: 2, 82: 2, 83: 2, 84: 2, 85: 2, 86: 2, 87: 2, 88: 2, 89: 2, 90: 2, 91: 2, 92: 2, 93: 2, 94: 2, 95: 2, 96: 2, 97: 2, 98: 2, 99: 2, 100: 2})
        self.assertEqual(experiment.stimblock, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 2, 27: 2, 28: 2, 29: 2, 30: 2, 31: 2, 32: 2, 33: 2, 34: 2, 35: 2, 36: 2, 37: 2, 38: 2, 39: 2, 40: 2, 41: 2, 42: 2, 43: 2, 44: 2, 45: 2, 46: 2, 47: 2, 48: 2,
                                                49: 2, 50: 2, 51: 3, 52: 3, 53: 3, 54: 3, 55: 3, 56: 3, 57: 3, 58: 3, 59: 3, 60: 3, 61: 3, 62: 3, 63: 3, 64: 3, 65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3, 74: 3, 75: 3, 76: 4, 77: 4, 78: 4, 79: 4, 80: 4, 81: 4, 82: 4, 83: 4, 84: 4, 85: 4, 86: 4, 87: 4, 88: 4, 89: 4, 90: 4, 91: 4, 92: 4, 93: 4, 94: 4, 95: 4, 96: 4, 97: 4, 98: 4, 99: 4, 100: 4})
        self.assertEqual(experiment.stimtrial, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 1, 27: 2, 28: 3, 29: 4, 30: 5, 31: 6, 32: 7, 33: 8, 34: 9, 35: 10, 36: 11, 37: 12, 38: 13, 39: 14, 40: 15, 41: 16, 42: 17, 43: 18, 44: 19, 45: 20, 46: 21, 47: 22, 48: 23,
                                                49: 24, 50: 25, 51: 1, 52: 2, 53: 3, 54: 4, 55: 5, 56: 6, 57: 7, 58: 8, 59: 9, 60: 10, 61: 11, 62: 12, 63: 13, 64: 14, 65: 15, 66: 16, 67: 17, 68: 18, 69: 19, 70: 20, 71: 21, 72: 22, 73: 23, 74: 24, 75: 25, 76: 1, 77: 2, 78: 3, 79: 4, 80: 5, 81: 6, 82: 7, 83: 8, 84: 9, 85: 10, 86: 11, 87: 12, 88: 13, 89: 14, 90: 15, 91: 16, 92: 17, 93: 18, 94: 19, 95: 20, 96: 21, 97: 22, 98: 23, 99: 24, 100: 25})
        self.assertEqual(len(experiment.stimlist), 100)
        self.assertEqual(experiment.last_N, 0)
        self.assertEqual(experiment.end_at, {1: 51, 2: 51, 3: 51, 4: 51, 5: 51, 6: 51, 7: 51, 8: 51, 9: 51, 10: 51, 11: 51, 12: 51, 13: 51, 14: 51, 15: 51, 16: 51, 17: 51, 18: 51, 19: 51, 20: 51, 21: 51, 22: 51, 23: 51, 24: 51, 25: 51, 26: 51, 27: 51, 28: 51, 29: 51, 30: 51, 31: 51, 32: 51, 33: 51, 34: 51, 35: 51, 36: 51, 37: 51, 38: 51, 39: 51, 40: 51, 41: 51, 42: 51, 43: 51, 44: 51, 45: 51, 46: 51, 47: 51, 48: 51, 49: 51, 50: 51, 51: 101, 52: 101,
                                             53: 101, 54: 101, 55: 101, 56: 101, 57: 101, 58: 101, 59: 101, 60: 101, 61: 101, 62: 101, 63: 101, 64: 101, 65: 101, 66: 101, 67: 101, 68: 101, 69: 101, 70: 101, 71: 101, 72: 101, 73: 101, 74: 101, 75: 101, 76: 101, 77: 101, 78: 101, 79: 101, 80: 101, 81: 101, 82: 101, 83: 101, 84: 101, 85: 101, 86: 101, 87: 101, 88: 101, 89: 101, 90: 101, 91: 101, 92: 101, 93: 101, 94: 101, 95: 101, 96: 101, 97: 101, 98: 101, 99: 101, 100: 101})
        self.assertEqual(experiment.stimpr, {1: 'random', 2: 'random', 3: 'random', 4: 'random', 5: 'random', 6: 'pattern', 7: 'random', 8: 'pattern', 9: 'random', 10: 'pattern', 11: 'random', 12: 'pattern', 13: 'random', 14: 'pattern', 15: 'random', 16: 'pattern', 17: 'random', 18: 'pattern', 19: 'random', 20: 'pattern', 21: 'random', 22: 'pattern', 23: 'random', 24: 'pattern', 25: 'random', 26: 'random', 27: 'random', 28: 'random', 29: 'random', 30: 'random', 31: 'pattern', 32: 'random', 33: 'pattern', 34: 'random', 35: 'pattern', 36: 'random', 37: 'pattern', 38: 'random', 39: 'pattern', 40: 'random', 41: 'pattern', 42: 'random', 43: 'pattern', 44: 'random', 45: 'pattern', 46: 'random', 47: 'pattern', 48: 'random', 49: 'pattern',
                                             50: 'random', 51: 'random', 52: 'random', 53: 'random', 54: 'random', 55: 'random', 56: 'pattern', 57: 'random', 58: 'pattern', 59: 'random', 60: 'pattern', 61: 'random', 62: 'pattern', 63: 'random', 64: 'pattern', 65: 'random', 66: 'pattern', 67: 'random', 68: 'pattern', 69: 'random', 70: 'pattern', 71: 'random', 72: 'pattern', 73: 'random', 74: 'pattern', 75: 'random', 76: 'random', 77: 'random', 78: 'random', 79: 'random', 80: 'random', 81: 'pattern', 82: 'random', 83: 'pattern', 84: 'random', 85: 'pattern', 86: 'random', 87: 'pattern', 88: 'random', 89: 'pattern', 90: 'random', 91: 'pattern', 92: 'random', 93: 'pattern', 94: 'random', 95: 'pattern', 96: 'random', 97: 'pattern', 98: 'random', 99: 'pattern', 100: 'random'})

        # Check person data handler's properties too
        self.assertEqual(experiment.person_data.subject_id,
                         "subject_10_kontrol")
        self.assertEqual(experiment.person_data.all_settings_file_path, os.path.join(
            thispath, "subject_settings", experiment.person_data.subject_id))
        self.assertEqual(experiment.person_data.all_IDs_file_path, os.path.join(
            thispath, "subject_settings", "participant_settings"))
        self.assertEqual(experiment.person_data.subject_list_file_path, os.path.join(
            thispath, "subject_settings", "participants_in_experiment.txt"))
        self.assertEqual(experiment.person_data.output_file_path, os.path.join(
            thispath, "logs", experiment.person_data.subject_id + "_log.txt"))

        # Some files were created
        self.assertTrue(os.path.isfile(experiment.person_data.all_settings_file_path + ".dat") or
                        os.path.isfile(experiment.person_data.all_settings_file_path))
        self.assertTrue(os.path.isfile(experiment.person_data.all_IDs_file_path + ".dat") or
                        os.path.isfile(experiment.person_data.all_IDs_file_path))
        self.assertTrue(os.path.isfile(
            experiment.person_data.subject_list_file_path))

    def testExistingSettingsFile(self):
        gui_mock = pgm.PsychoPyGuiMock()
        gui_mock.addFieldValues(
            [10, 'kontrol', 'nő', 30, '3rd', '2nd', 10, 'kontrol'])

        thispath = self.constructFilePath("NoSettingsFile")
        experiment = asrt.Experiment(thispath)
        experiment.settings = asrt.ExperimentSettings("", "")
        experiment.settings.groups = ["kontrol", "exp1"]
        experiment.settings.numsessions = 2
        experiment.settings.epochN = 2
        experiment.settings.epochs = [1, 1]
        experiment.settings.block_in_epochN = 2
        experiment.settings.blockprepN = 5
        experiment.settings.blocklengthN = 20
        experiment.settings.asrt_rcolor = "Orange"
        experiment.settings.asrt_pcolor = "Green"
        experiment.settings.asrt_types = {}
        experiment.settings.asrt_types[1] = "implicit"
        experiment.settings.asrt_types[2] = "implicit"

        asrt.ensure_dir(os.path.join(thispath, "subject_settings"))

        # call once to get the participant settings
        experiment.participant_id()

        # let save participant settings after the first block
        experiment.last_N = 25
        experiment.person_data.save_person_settings(experiment)

        experiment.settings = asrt.ExperimentSettings("", "")
        experiment.settings.groups = ["kontrol", "exp1"]
        experiment.settings.epochN = 2
        experiment.settings.block_in_epochN = 2
        experiment.settings.blockprepN = 5
        experiment.settings.blocklengthN = 20

        # now load back the participant's settings with participant id function
        experiment.participant_id()

        self.assertEqual(experiment.subject_group, 'kontrol')
        self.assertEqual(experiment.subject_number, 10)
        self.assertEqual(experiment.PCodes, {1: '3rd - 1324', 2: '2nd - 1243'})
        self.assertEqual(experiment.stim_output_line, 0)
        self.assertEqual(experiment.stim_sessionN, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1,
                                                    49: 1, 50: 1, 51: 2, 52: 2, 53: 2, 54: 2, 55: 2, 56: 2, 57: 2, 58: 2, 59: 2, 60: 2, 61: 2, 62: 2, 63: 2, 64: 2, 65: 2, 66: 2, 67: 2, 68: 2, 69: 2, 70: 2, 71: 2, 72: 2, 73: 2, 74: 2, 75: 2, 76: 2, 77: 2, 78: 2, 79: 2, 80: 2, 81: 2, 82: 2, 83: 2, 84: 2, 85: 2, 86: 2, 87: 2, 88: 2, 89: 2, 90: 2, 91: 2, 92: 2, 93: 2, 94: 2, 95: 2, 96: 2, 97: 2, 98: 2, 99: 2, 100: 2})
        self.assertEqual(experiment.stimepoch, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 41: 1, 42: 1, 43: 1, 44: 1, 45: 1, 46: 1, 47: 1, 48: 1,
                                                49: 1, 50: 1, 51: 2, 52: 2, 53: 2, 54: 2, 55: 2, 56: 2, 57: 2, 58: 2, 59: 2, 60: 2, 61: 2, 62: 2, 63: 2, 64: 2, 65: 2, 66: 2, 67: 2, 68: 2, 69: 2, 70: 2, 71: 2, 72: 2, 73: 2, 74: 2, 75: 2, 76: 2, 77: 2, 78: 2, 79: 2, 80: 2, 81: 2, 82: 2, 83: 2, 84: 2, 85: 2, 86: 2, 87: 2, 88: 2, 89: 2, 90: 2, 91: 2, 92: 2, 93: 2, 94: 2, 95: 2, 96: 2, 97: 2, 98: 2, 99: 2, 100: 2})
        self.assertEqual(experiment.stimblock, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 2, 27: 2, 28: 2, 29: 2, 30: 2, 31: 2, 32: 2, 33: 2, 34: 2, 35: 2, 36: 2, 37: 2, 38: 2, 39: 2, 40: 2, 41: 2, 42: 2, 43: 2, 44: 2, 45: 2, 46: 2, 47: 2, 48: 2,
                                                49: 2, 50: 2, 51: 3, 52: 3, 53: 3, 54: 3, 55: 3, 56: 3, 57: 3, 58: 3, 59: 3, 60: 3, 61: 3, 62: 3, 63: 3, 64: 3, 65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3, 74: 3, 75: 3, 76: 4, 77: 4, 78: 4, 79: 4, 80: 4, 81: 4, 82: 4, 83: 4, 84: 4, 85: 4, 86: 4, 87: 4, 88: 4, 89: 4, 90: 4, 91: 4, 92: 4, 93: 4, 94: 4, 95: 4, 96: 4, 97: 4, 98: 4, 99: 4, 100: 4})
        self.assertEqual(experiment.stimtrial, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 1, 27: 2, 28: 3, 29: 4, 30: 5, 31: 6, 32: 7, 33: 8, 34: 9, 35: 10, 36: 11, 37: 12, 38: 13, 39: 14, 40: 15, 41: 16, 42: 17, 43: 18, 44: 19, 45: 20, 46: 21, 47: 22, 48: 23,
                                                49: 24, 50: 25, 51: 1, 52: 2, 53: 3, 54: 4, 55: 5, 56: 6, 57: 7, 58: 8, 59: 9, 60: 10, 61: 11, 62: 12, 63: 13, 64: 14, 65: 15, 66: 16, 67: 17, 68: 18, 69: 19, 70: 20, 71: 21, 72: 22, 73: 23, 74: 24, 75: 25, 76: 1, 77: 2, 78: 3, 79: 4, 80: 5, 81: 6, 82: 7, 83: 8, 84: 9, 85: 10, 86: 11, 87: 12, 88: 13, 89: 14, 90: 15, 91: 16, 92: 17, 93: 18, 94: 19, 95: 20, 96: 21, 97: 22, 98: 23, 99: 24, 100: 25})
        self.assertEqual(len(experiment.stimlist), 100)
        self.assertEqual(experiment.last_N, 25)
        self.assertEqual(experiment.end_at, {1: 51, 2: 51, 3: 51, 4: 51, 5: 51, 6: 51, 7: 51, 8: 51, 9: 51, 10: 51, 11: 51, 12: 51, 13: 51, 14: 51, 15: 51, 16: 51, 17: 51, 18: 51, 19: 51, 20: 51, 21: 51, 22: 51, 23: 51, 24: 51, 25: 51, 26: 51, 27: 51, 28: 51, 29: 51, 30: 51, 31: 51, 32: 51, 33: 51, 34: 51, 35: 51, 36: 51, 37: 51, 38: 51, 39: 51, 40: 51, 41: 51, 42: 51, 43: 51, 44: 51, 45: 51, 46: 51, 47: 51, 48: 51, 49: 51, 50: 51, 51: 101, 52: 101,
                                             53: 101, 54: 101, 55: 101, 56: 101, 57: 101, 58: 101, 59: 101, 60: 101, 61: 101, 62: 101, 63: 101, 64: 101, 65: 101, 66: 101, 67: 101, 68: 101, 69: 101, 70: 101, 71: 101, 72: 101, 73: 101, 74: 101, 75: 101, 76: 101, 77: 101, 78: 101, 79: 101, 80: 101, 81: 101, 82: 101, 83: 101, 84: 101, 85: 101, 86: 101, 87: 101, 88: 101, 89: 101, 90: 101, 91: 101, 92: 101, 93: 101, 94: 101, 95: 101, 96: 101, 97: 101, 98: 101, 99: 101, 100: 101})
        self.assertEqual(experiment.stimpr, {1: 'random', 2: 'random', 3: 'random', 4: 'random', 5: 'random', 6: 'pattern', 7: 'random', 8: 'pattern', 9: 'random', 10: 'pattern', 11: 'random', 12: 'pattern', 13: 'random', 14: 'pattern', 15: 'random', 16: 'pattern', 17: 'random', 18: 'pattern', 19: 'random', 20: 'pattern', 21: 'random', 22: 'pattern', 23: 'random', 24: 'pattern', 25: 'random', 26: 'random', 27: 'random', 28: 'random', 29: 'random', 30: 'random', 31: 'pattern', 32: 'random', 33: 'pattern', 34: 'random', 35: 'pattern', 36: 'random', 37: 'pattern', 38: 'random', 39: 'pattern', 40: 'random', 41: 'pattern', 42: 'random', 43: 'pattern', 44: 'random', 45: 'pattern', 46: 'random', 47: 'pattern', 48: 'random', 49: 'pattern',
                                             50: 'random', 51: 'random', 52: 'random', 53: 'random', 54: 'random', 55: 'random', 56: 'pattern', 57: 'random', 58: 'pattern', 59: 'random', 60: 'pattern', 61: 'random', 62: 'pattern', 63: 'random', 64: 'pattern', 65: 'random', 66: 'pattern', 67: 'random', 68: 'pattern', 69: 'random', 70: 'pattern', 71: 'random', 72: 'pattern', 73: 'random', 74: 'pattern', 75: 'random', 76: 'random', 77: 'random', 78: 'random', 79: 'random', 80: 'random', 81: 'pattern', 82: 'random', 83: 'pattern', 84: 'random', 85: 'pattern', 86: 'random', 87: 'pattern', 88: 'random', 89: 'pattern', 90: 'random', 91: 'pattern', 92: 'random', 93: 'pattern', 94: 'random', 95: 'pattern', 96: 'random', 97: 'pattern', 98: 'random', 99: 'pattern', 100: 'random'})


if __name__ == "__main__":
    unittest.main()  # run all tests
