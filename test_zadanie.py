from zadanie import * 


def test_hello(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "Hello world from dev\n"
