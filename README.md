# ConanFile for Fine Free File Command
See https://www.darwinsys.com/file for more information on the library.

# Building and Uploading

```
conan create . --build
conan upload -c "file/*" -r <your-remote>
```

# Using in CMake
```
conan_cmake_configure(REQUIRES file/5.40 GENERATORS cmake_find_package)
...

find_package(file REQUIRED)
...
```
