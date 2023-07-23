.PHONY: vuln-check
vuln-check:
	@govulncheck .

.PHONY: build
build:
	@make vuln-check && @go build -o test
