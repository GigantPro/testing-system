.. raw:: html

   <p align="center">
        <h1 align="center"><a href="https://edu.xiver.ru/">Education.Xiver</a></h1>
        <h2 align="center">Этот проект нужен для эффективной учебы и облегчения раброты учителям!</h2>
    </p>

    <p align="center">
        <h3 align="center"><b>!Продукт находится в разработке и не показывает итоговый вариант!</b></h3>
    </p>

=========

Developing
^^^^^^^^^^

*Dependencies*:

* `make`
* `docker-compose`
* `docker`

.. code-block:: shell

    git clone https://github.com/xiver-org/testing-system.git; cd testing-system-master
    cp .env.example .env.dev
    make


Prodaction
^^^^^^^^^^

*Dependencies*:

* `make`
* `docker-compose`
* `docker`

.. code-block:: shell

    git clone https://github.com/xiver-org/testing-system.git; cd testing-system-master
    cp .env.example .env
    make DEV=0
