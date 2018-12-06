DESTDIR	=
BINDIR	= /usr/bin
CONFDIR = /etc

sample: sample.c
	gcc -o sample sample.c

.PHONY: install
install: sample
	install -d -m 0755 ${DESTDIR}${BINDIR}
	install -m 0755 sample ${DESTDIR}${BINDIR}/
	install -d -m 0755 ${DESTDIR}${CONFDIR}/sample
	install -m 0644 sample.cnof ${DESTDIR}${CONFDIR}/sample/sample.conf

.PHONY: check
check:
	${DESTDIR}${BINDIR}/sample

.PHONY: clean
clean:
	rm -rf sample
