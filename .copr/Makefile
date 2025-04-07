.PHONY: srpm

srpm:
	mkdir -p $(outdir)
	mkdir -p SOURCES
	rpmbuild -bs \
		--define "_sourcedir $(PWD)/SOURCES" \
		--define "_specdir $(PWD)/SPECS" \
		--define "_builddir $(PWD)/BUILD" \
		--define "_srcrpmdir $(outdir)" \
		--define "_rpmdir $(PWD)/RPMS" \
		--define "_buildrootdir $(PWD)/BUILDROOT" \
		SPECS/troll.spec

	# Find the srpm
	find $(outdir) -name "*.src.rpm" -o -name "*.nosrc.rpm"
