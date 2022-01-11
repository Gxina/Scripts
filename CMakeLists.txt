cmake_minimum_required(VERSION 3.21)
project(langageC C)

set(CMAKE_C_STANDARD 99)

add_executable(langageC payload.h personnage.c personnage.h personnages.txt)
