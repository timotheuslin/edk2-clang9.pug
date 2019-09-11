all :: build

project_py	=	python project.py

build ::
	$(project_py)

clean ::
	$(project_py) clean

cleanall ::
	$(project_py) cleanall

.PHONY: all clean cleanall build
