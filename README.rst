==========
rst2txtast
==========

.. note:: 用途を考慮して、README等は日本語メインでの記載となります。

概要
====

docutilsを通して、reStructuredTextなどから TxtAST(ltextlintが内部処理に使用するAST)を生成するCLIです。

このリポジトリは、
`@jimo1001 <https://github.com/johejo/>`_ の https://github.com/jimo1001/docutils-ast-writer をフォークして公開されていた、
`@shiguredo <https://github.com/shiguredo/>`_ の https://github.com/shiguredo/docutils-ast-writer をフォークしたものです。

PyPIへの登録を想定しており、コマンド名とパッケージ名を変更して運用しています。

インストール
============

現在は、PyPIへの登録を行っていません。

.. code-block:: console

   $ pip install -e git+https://github.com/atsphinx/rst2txtast

使い方
======

.. code-block:: console

   $ rst2txtast [options] [<source> [<destination>]]


ライセンス
==========

MITライセンスの下で公開されています。
