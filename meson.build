project('asd-lab', 'cpp', default_options: ['cpp_std=c++17', 'buildtype=release', 'warning_level=3'])
lab = executable('asd-lab', 'src/main.cpp')
test('correctness', lab, args: ['--check'])
