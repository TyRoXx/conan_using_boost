from conans import ConanFile, CMake

class ConanUsingBoost(ConanFile):
	settings = "os", "compiler", "build_type", "arch"
	requires = "Boost/1.59.0@lasote/stable"
	generators = "cmake"
