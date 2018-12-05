.PHONY: usage
usage:
	@echo 'bp       prep'
	@echo 'bc       prep build'
	@echo 'bi       prep build install'
	@echo 'bb       prep build install make rpm'
	@echo 'rpm      prep build install make rpm'
	@echo ''
	@echo 'clean    clean directory'

.PHONY: bp bc bi bb bs
bp bc bi bb bs: deploy
	rpmbuild -v -$@ SPECS/sample.spec

.PHONY: rpm
rpm: deploy
	${MAKE} -s bb

.PHONY: clean
clean:
	rm -rf BUILD BUILDROOT RPMS SRPMS

.PHONY: deploy
deploy:
	@tar zcf sample-script-1.0.tar.gz sample-script-1.0
	@mv -v *.tar.gz SOURCES/
