# CPP

## CPP 调用Python

```cpp

#include <iostream>
#include <Python.h>

using namespace std;

int main()
{
    std::cout << "start" << endl;
    Py_Initialize();

    if (!Py_IsInitialized())
    {
        printf("初始化失败！");
        return 0;
    }

    PyRun_SimpleString("import os, sys");
    PyRun_SimpleString("sys.path.append('./')");
    PyRun_SimpleString("sys.path.append('D:/project/Observer/Lib/site-packages/')");
    PyRun_SimpleString("sys.path.append('D:/project/Observer/Lib/')");
    PyRun_SimpleString("import pyautogui");
    PyRun_SimpleString("print(os.getcwd())");

    PyObject* pModule = NULL;
    PyObject* pFunction = NULL;

    pModule = PyImport_ImportModule("observer");
    if (pModule == NULL)
    {
        cout << "未找到" <<endl;
        system("pause");
        return -1;
    }

    pFunction = PyObject_GetAttrString(pModule, "screen_shot");
    PyObject* pRet = PyObject_CallObject(pFunction, NULL);
    
    std::string res = PyUnicode_AsUTF8(pRet);
    cout << res;
    Py_Finalize();
    system("pause");
}



```