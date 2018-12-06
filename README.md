# smaple-script

# 概要

specファイルを書いてrpmパッケージを作るのに用いたプログラム。
簡単なCプログラムをパッケージングして`yum`や`rpm`コマンドでインストールできるようにしている。

# Require

* OS
  * CentOS7を用いて開発。試して無いけどRHELでもいけると思う。

* 依存パッケージ
  * rpmbuild
  * gcc
  * make

# 使い方

`Makefile`を書いているので`make`コマンドで色々できる。

``` console
$ make
bp       prep
bc       prep build
bi       prep build install
bb       prep build install make rpm
rpm      prep build install make rpm

clean    clean directory
```

* パッケージの作成

``` console
$ make rpm
```

`RPMS`ディレクトリ配下にrpmパッケージファイルができます。

* パッケージのインストール

``` console
$ sudo yum localinstall RPMS/x86_64/sample-script-1.0-1.el7.x86_64.rpm
```
