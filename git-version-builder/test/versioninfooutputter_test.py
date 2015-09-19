import unittest

from gitversionbuilder import versioninfo
from gitversionbuilder import versioninfooutputter
import test_utils


class VersionInfoOutputterTest(unittest.TestCase, test_utils.CodeAsserts):
    def test_output_cpp(self):
        expected = """
                // ---------------------------------------------------
                // This file is autogenerated by git-version.
                // DO NOT MODIFY!
                // ---------------------------------------------------

                #pragma once
                #ifndef MESSMER_GITVERSION_VERSION_H
                #define MESSMER_GITVERSION_VERSION_H

                namespace version {
                    constexpr const char *VERSION_STRING = "versionone-dev2-230a";
                    constexpr const char *GIT_TAG_NAME = "versionone";
                    constexpr const unsigned int GIT_COMMITS_SINCE_TAG = 2;
                    constexpr const char *GIT_COMMIT_ID = "230a";
                    constexpr bool IS_DEV_VERSION = true;
                }

                #endif
            """
        actual = versioninfooutputter.to_cpp(versioninfo.VersionInfo("versionone", 2, "230a", True))
        self.assertCodeEqual(expected, actual)

    def test_output_cpp_without_tag(self):
        expected = """
                // ---------------------------------------------------
                // This file is autogenerated by git-version.
                // DO NOT MODIFY!
                // ---------------------------------------------------

                #pragma once
                #ifndef MESSMER_GITVERSION_VERSION_H
                #define MESSMER_GITVERSION_VERSION_H

                namespace version {
                    constexpr const char *VERSION_STRING = "dev2-230a";
                    constexpr const char *GIT_TAG_NAME = "develop";
                    constexpr const unsigned int GIT_COMMITS_SINCE_TAG = 2;
                    constexpr const char *GIT_COMMIT_ID = "230a";
                    constexpr bool IS_DEV_VERSION = true;
                    constexpr bool IS_STABLE_VERSION = false;
                }

                #endif
            """
        actual = versioninfooutputter.to_cpp(versioninfo.VersionInfo("develop", 2, "230a", False))
        self.assertCodeEqual(expected, actual)

    def test_output_cpp_with_version_info(self):
        expected = """
                // ---------------------------------------------------
                // This file is autogenerated by git-version.
                // DO NOT MODIFY!
                // ---------------------------------------------------

                #pragma once
                #ifndef MESSMER_GITVERSION_VERSION_H
                #define MESSMER_GITVERSION_VERSION_H

                namespace version {
                    constexpr const char *VERSION_STRING = "1.6-dev2-230a";
                    constexpr const char *GIT_TAG_NAME = "1.6";
                    constexpr const unsigned int GIT_COMMITS_SINCE_TAG = 2;
                    constexpr const char *GIT_COMMIT_ID = "230a";
                    constexpr bool IS_DEV_VERSION = true;
                    constexpr bool IS_STABLE_VERSION = false;

                    constexpr const char *VERSION_COMPONENTS[] = {"1", "6"};
                    constexpr const char *VERSION_TAG = "";
                }

                #endif
            """
        actual = versioninfooutputter.to_cpp(versioninfo.VersionInfo("1.6", 2, "230a", True))
        self.assertCodeEqual(expected, actual)

    def test_output_cpp_with_version_info_with_leading_zero(self):
        expected = """
                // ---------------------------------------------------
                // This file is autogenerated by git-version.
                // DO NOT MODIFY!
                // ---------------------------------------------------

                #pragma once
                #ifndef MESSMER_GITVERSION_VERSION_H
                #define MESSMER_GITVERSION_VERSION_H

                namespace version {
                    constexpr const char *VERSION_STRING = "1.06-dev2-230a";
                    constexpr const char *GIT_TAG_NAME = "1.06";
                    constexpr const unsigned int GIT_COMMITS_SINCE_TAG = 2;
                    constexpr const char *GIT_COMMIT_ID = "230a";
                    constexpr bool IS_DEV_VERSION = true;
                    constexpr bool IS_STABLE_VERSION = false;

                    constexpr const char *VERSION_COMPONENTS[] = {"1", "06"};
                    constexpr const char *VERSION_TAG = "";
                }

                #endif
            """
        actual = versioninfooutputter.to_cpp(versioninfo.VersionInfo("1.06", 2, "230a", True))
        self.assertCodeEqual(expected, actual)

    def test_output_cpp_with_version_info_and_version_tag(self):
        expected = """
                // ---------------------------------------------------
                // This file is autogenerated by git-version.
                // DO NOT MODIFY!
                // ---------------------------------------------------

                #pragma once
                #ifndef MESSMER_GITVERSION_VERSION_H
                #define MESSMER_GITVERSION_VERSION_H

                namespace version {
                    constexpr const char *VERSION_STRING = "1.6alpha-dev2-230a";
                    constexpr const char *GIT_TAG_NAME = "1.6alpha";
                    constexpr const unsigned int GIT_COMMITS_SINCE_TAG = 2;
                    constexpr const char *GIT_COMMIT_ID = "230a";
                    constexpr bool IS_DEV_VERSION = true;
                    constexpr bool IS_STABLE_VERSION = false;

                    constexpr const char *VERSION_COMPONENTS[] = {"1", "6"};
                    constexpr const char *VERSION_TAG = "alpha";
                }

                #endif
            """
        actual = versioninfooutputter.to_cpp(versioninfo.VersionInfo("1.6alpha", 2, "230a", True))
        self.assertCodeEqual(expected, actual)

    def test_output_cpp_with_version_info_and_dashed_version_tag(self):
        expected = """
                // ---------------------------------------------------
                // This file is autogenerated by git-version.
                // DO NOT MODIFY!
                // ---------------------------------------------------

                #pragma once
                #ifndef MESSMER_GITVERSION_VERSION_H
                #define MESSMER_GITVERSION_VERSION_H

                namespace version {
                    constexpr const char *VERSION_STRING = "1.6-alpha-dev2-230a";
                    constexpr const char *GIT_TAG_NAME = "1.6-alpha";
                    constexpr const unsigned int GIT_COMMITS_SINCE_TAG = 2;
                    constexpr const char *GIT_COMMIT_ID = "230a";
                    constexpr bool IS_DEV_VERSION = true;
                    constexpr bool IS_STABLE_VERSION = false;

                    constexpr const char *VERSION_COMPONENTS[] = {"1", "6"};
                    constexpr const char *VERSION_TAG = "alpha";
                }

                #endif
            """
        actual = versioninfooutputter.to_cpp(versioninfo.VersionInfo("1.6-alpha", 2, "230a", True))
        self.assertCodeEqual(expected, actual)

    def test_output_python(self):
        expected = """
                # ---------------------------------------------------
                # This file is autogenerated by git-version.
                # DO NOT MODIFY!
                # ---------------------------------------------------

                VERSION_STRING = "versiontwo-dev2-230a"
                GIT_TAG_NAME = "versiontwo"
                GIT_COMMITS_SINCE_TAG = 2
                GIT_COMMIT_ID = "230a"
                IS_DEV_VERSION = True
            """
        actual = versioninfooutputter.to_python(versioninfo.VersionInfo("versiontwo", 2, "230a", True))
        self.assertCodeEqual(expected, actual)

    def test_output_python_with_version_info(self):
        expected = """
                # ---------------------------------------------------
                # This file is autogenerated by git-version.
                # DO NOT MODIFY!
                # ---------------------------------------------------

                VERSION_STRING = "0.8-dev2-230a"
                GIT_TAG_NAME = "0.8"
                GIT_COMMITS_SINCE_TAG = 2
                GIT_COMMIT_ID = "230a"
                IS_DEV_VERSION = True
                IS_STABLE_VERSION = False

                VERSION_COMPONENTS = ["0", "8"]
                VERSION_TAG = ""
            """
        actual = versioninfooutputter.to_python(versioninfo.VersionInfo("0.8", 2, "230a", True))
        self.assertCodeEqual(expected, actual)

    def test_output_python_with_version_info_and_version_tag(self):
        expected = """
                # ---------------------------------------------------
                # This file is autogenerated by git-version.
                # DO NOT MODIFY!
                # ---------------------------------------------------

                VERSION_STRING = "v1.0alpha-dev2-230a"
                GIT_TAG_NAME = "v1.0alpha"
                GIT_COMMITS_SINCE_TAG = 2
                GIT_COMMIT_ID = "230a"
                IS_DEV_VERSION = True
                IS_STABLE_VERSION = False

                VERSION_COMPONENTS = ["1", "0"]
                VERSION_TAG = "alpha"
            """
        actual = versioninfooutputter.to_python(versioninfo.VersionInfo("v1.0alpha", 2, "230a", True))
        self.assertCodeEqual(expected, actual)

    def test_output_python_instable_nondev(self):
        expected = """
                # ---------------------------------------------------
                # This file is autogenerated by git-version.
                # DO NOT MODIFY!
                # ---------------------------------------------------

                VERSION_STRING = "v1.0alpha"
                GIT_TAG_NAME = "v1.0alpha"
                GIT_COMMITS_SINCE_TAG = 0
                GIT_COMMIT_ID = "230a"
                IS_DEV_VERSION = False
                IS_STABLE_VERSION = False

                VERSION_COMPONENTS = ["1", "0"]
                VERSION_TAG = "alpha"
            """
        actual = versioninfooutputter.to_python(versioninfo.VersionInfo("v1.0alpha", 0, "230a", True))
        self.assertCodeEqual(expected, actual)

    def test_output_python_stable_nondev_plain(self):
        expected = """
                # ---------------------------------------------------
                # This file is autogenerated by git-version.
                # DO NOT MODIFY!
                # ---------------------------------------------------

                VERSION_STRING = "v1.0"
                GIT_TAG_NAME = "v1.0"
                GIT_COMMITS_SINCE_TAG = 0
                GIT_COMMIT_ID = "230a"
                IS_DEV_VERSION = False
                IS_STABLE_VERSION = True

                VERSION_COMPONENTS = ["1", "0"]
                VERSION_TAG = ""
            """
        actual = versioninfooutputter.to_python(versioninfo.VersionInfo("v1.0", 0, "230a", True))
        self.assertCodeEqual(expected, actual)

    def test_output_python_stable_stable(self):
        expected = """
                # ---------------------------------------------------
                # This file is autogenerated by git-version.
                # DO NOT MODIFY!
                # ---------------------------------------------------

                VERSION_STRING = "v1.0-stable"
                GIT_TAG_NAME = "v1.0-stable"
                GIT_COMMITS_SINCE_TAG = 0
                GIT_COMMIT_ID = "230a"
                IS_DEV_VERSION = False
                IS_STABLE_VERSION = True

                VERSION_COMPONENTS = ["1", "0"]
                VERSION_TAG = "stable"
            """
        actual = versioninfooutputter.to_python(versioninfo.VersionInfo("v1.0-stable", 0, "230a", True))
        self.assertCodeEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
