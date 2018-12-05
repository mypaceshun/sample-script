DESTDIR	=
BINDIR	= /usr/bin

sample: sample.c
	gcc -o sample sample.c

.PHONY: install
install: sample
	install -d -m 0755 ${DESTDIR}${BINDIR}
	install -m 0755 sample ${DESTDIR}${BINDIR}/

.PHONY: check
check:
	${DESTDIR}${BINDIR}/sample

.PHONY: clean
clean:
	rm -rf sample
