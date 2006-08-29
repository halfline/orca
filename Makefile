# Makefile for source rpm: orca
# $Id$
NAME := orca
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
