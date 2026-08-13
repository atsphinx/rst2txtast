==========
rst2txtast
==========

.. note:: 用途を考慮して、README等は日本語メインでの記載となります。

概要
====

docutilsを通して、reStructuredTextなどから TxtAST(ltextlintが内部処理に使用するAST)を生成するCLIです。
textlint用プラグインである `textlint-plugin-rst <https://www.npmjs.com/package/textlint-plugin-rst>`_ から呼びだされることを想定しています。

このリポジトリは、
`@jimo1001 <https://github.com/jimo1001/>`_ の https://github.com/jimo1001/docutils-ast-writer をフォークして公開されていた、
`@shiguredo <https://github.com/shiguredo/>`_ の https://github.com/shiguredo/docutils-ast-writer をフォークしたものです。

PyPIへの登録を想定しており、コマンド名とパッケージ名を変更して運用しています。

インストール
============

現在は、PyPIへの登録を行っていません。

.. code-block:: console

   $ pip install -e git+https://github.com/atsphinx/rst2txtast

TestPyPI上にはアップロードされているため、Gitリポジトリの指定をしたくないのであれば下記のコマンドを推奨します。

.. code-block:: console

   $ pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ rst2txtast

.. note::

   uvでプロジェクトを管理している場合、 ``pyproject.toml`` に下記の記述をして ``uv add rst2txtast`` と実行してください。

   .. code:: toml

      [tool.uv.sources]
      rst2txtast = { index = "testpypi" }

      [[tool.uv.index]]
      name = "testpypi"
      url = "https://test.pypi.org/simple/"
      explicit = true

使い方
======

.. code-block:: console

   $ rst2txtast [options] [<source> [<destination>]]


ライセンス
==========

MITライセンスの下で公開されています。
