# fishmlserv

## fastapi Creating

### Deploy
![image](https://github.com/user-attachments/assets/a2665a21-109f-415b-a974-06495ce8d23d)


### Run
- dev
- http://localhost:8000/docs
```bash
# uvicorn --help
$ uvicorn src.fishmlserv.main:app --reload
```
- prd
```bash
$ uvicorn src.fishmlserv.main:app --host 0.0.0.0 --port 8949
```
