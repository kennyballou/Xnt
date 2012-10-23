#!/usr/bin/env python

import sys
import os
import shutil
import xnt.tasks
import unittest


class TaskTests(unittest.TestCase):
    def setUp(self):
        os.mkdir("temp")
        os.mkdir("temp/testfolder1")
        for i in range(1, 5):
            with open("temp/testfile" + str(i), "w") as f:
                f.write("this is a test file")

    def tearDown(self):
        shutil.rmtree("temp")

    def test_cp(self):
        xnt.tasks.cp("temp/testfolder1", "temp/testfolder2")
        self.assertTrue(os.path.exists("temp/testfolder2"))
        self.assertTrue(os.path.exists("temp/testfolder1"))
        xnt.tasks.cp("temp/testfile1", "temp/testfile5")
        self.assertTrue(os.path.exists("temp/testfile5"))
        self.assertTrue(os.path.exists("temp/testfile1"))
        with open("temp/testfile5", "r") as testfile:
            self.assertEqual("this is a test file", testfile.read())

    def test_mv(self):
        xnt.tasks.mv("temp/testfolder1", "temp/testfolder2")
        self.assertTrue(os.path.exists("temp/testfolder2"))
        self.assertFalse(os.path.exists("temp/testfolder1"))
        xnt.tasks.mv("temp/testfile1", "temp/testfile5")
        self.assertTrue(os.path.exists("temp/testfile5"))
        self.assertFalse(os.path.exists("temp/testfile1"))
        with open("temp/testfile5", "r") as testfile:
            self.assertEqual("this is a test file", testfile.read())

    def test_mkdir(self):
        xnt.tasks.mkdir("temp/mynewtestfolder")
        self.assertTrue(os.path.exists("temp/mynewtestfolder"))

    def test_rm(self):
        xnt.tasks.rm("temp/testfolder1")
        self.assertFalse(os.path.exists("temp/testfolder1"))
        xnt.tasks.rm("temp/testfile1")
        self.assertFalse(os.path.exists("temp/testfile1"))
        xnt.tasks.rm("temp/testfile2",
                      "temp/testfile3",
                      "temp/testfile4")
        for i in range(1, 5):
            self.assertFalse(os.path.exists("temp/testfile" + str(i)))

    def test_zip(self):
        xnt.tasks.zip("temp/testfolder1", "temp/myzip.zip")
        self.assertTrue(os.path.exists("temp/myzip.zip"))

    def test_echo(self):
        xnt.tasks.echo("this is my cool echo", "temp/mynewcoolfile")
        self.assertTrue(os.path.exists("temp/mynewcoolfile"))
        with open("temp/mynewcoolfile", "r") as f:
            self.assertEqual("this is my cool echo", f.read())

if __name__ == "__main__":
    unittest.main()
