# sqlmesh-editable-repro

To reproduce, run

```shell
uv run sqlmesh plan
```

The error should be

```
Error: Failed to load model from file '/.../src/editable-repro/models/my_model.py':

  Object '<Logger editable_repro.my_module (INFO)>' cannot be serialized. If it's defined in a library, import the corresponding module and reference the object using its fully-qualified name. For example, the datetime module's 'UTC' object should be accessed as 'datetime.UTC'.
```

When the project is installed as a normal package, then it works as expected:

```
uv run --no-editable sqlmesh plan
```

To see the difference list the following files after each run:

```shell
ls -ld .venv/lib/python3.*/site-packages/*editable*
```
