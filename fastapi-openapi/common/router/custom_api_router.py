# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
)

import importlib

import types
import os
from dotenv import load_dotenv
load_dotenv()

DIR_PATH = os.environ['DIR_PATH']

from fastapi.routing import APIRoute

class CustomAPIRouter(APIRouter):
    def __init__(self):
        #pass
        super().__init__(route_class=APIRoute)

    def add_api_route(self, *args, **kwargs):

        args = self.replace_function(*args, **kwargs)
    #     # スーパークラスのメソッドを呼び出す
        super().add_api_route(*args, **kwargs)

    
    def replace_function(self,*args,**kwargs):
        """
        実行関数の入れ替え
        """
        # print(*args)
        # print(dict(kwargs))
        # print(args[1].__module__)
        # print(args[1].__name__)
        
        try:
            args_list = list(args)
            for i, arg in enumerate(args_list):
                if isinstance(arg, types.FunctionType):
                    endpoint = arg
                    index = i
                    break
            module_path = DIR_PATH + "." + endpoint.__module__
            function_name = endpoint.__name__

            #動的にfunctionを入れ替える　
            module = importlib.import_module(module_path)
            func = getattr(module,function_name)

            #入れ替え
            args_list[index] = func

            args = tuple(args_list)
            
            return args
        
        except ModuleNotFoundError as e:
            for i, arg in enumerate(args_list):
                if isinstance(arg, types.FunctionType):
                    endpoint = arg
            print("not custom api router:",endpoint.__module__+ "." +endpoint.__name__)
            return args
        
        except Exception as e:
            print("[ERROR]:",e)
            return args

