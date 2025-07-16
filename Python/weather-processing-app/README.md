# Weather Processing App

## Project Description
```
Course: ADEV-3005 Programming in Python
Instructor: Nico Cai
Section Number: 251409
Author: Mitchell Anonsen & Stefan Seeholzer
Date Created: March 19th,2024
Credit: 
Updates:
```

This application can be run to gather all available dates of data from Environment Canada for Winnipeg, Manitoba. The application will use the data gathered to create Box Plots or Line Plots of Max. Temp, Min. Temp, Mean Temp. This project can be used for anyone who needs to gather and use environmental data involving temperatures.


**Installation**: To install, download the WeatherProcessorInstaller.exe, for best results please Run installer as administrator. If you are unable to use admin privilege, please install to the proper user folder on your computer. Everything this application needs should already be part of the installer package, if issues arise please make sure you have updated all proper packages.

**Usage**: This application can be run to gather all available dates of data from Environment Canada for Winnipeg, Manitoba. On first use you will need to download weather data, which will create a sqlite DB and gather all currently available data from Environment Canada. PLEASE NOTE: As data downloads you can still create a plot or graph, however this program gathers the most recent dates first and works towards the last available dates. So if you need data further in the past, more time will be required to wait before it is available.

**Technologies Used**: Programming languages: Python



**Features**: This application will gather Specified data(Max Temp, Min Temp & Mean Temp) from Environment Canada. Once data is gathered you can create box plots for a range of years using the data, or a line graph for a specific month of a specified year and you are able to save the data.

**Contact Information**: You can contact us at manonsen@academic.rrc.ca

**Known Issues and Limitations**: Current Known issue is that installation MUST be ran as Administrator if installing to Program Files folder, if not ran as admin at the moment, Permission error creating log file in install folder is present. Another option is installing in to current users folder.

**Future Work**: Input to choose your preferred city from Environment Canada, as of right now location is hardcoded for testing and simplicity. 


### Pylint Result
************* Module weather_processor
weather_processor.py:17:0: E0401: Unable to import 'wx' (import-error)
weather_processor.py:35:4: R0914: Too many local variables (18/15) (too-many-locals)
weather_processor.py:112:19: W0718: Catching too general exception Exception (broad-exception-caught)
weather_processor.py:113:16: E1205: Too many arguments for logging format string (logging-too-many-args)
weather_processor.py:118:19: W0718: Catching too general exception Exception (broad-exception-caught)
weather_processor.py:119:16: E1205: Too many arguments for logging format string (logging-too-many-args)
weather_processor.py:156:23: W0718: Catching too general exception Exception (broad-exception-caught)
weather_processor.py:144:20: R1723: Unnecessary "else" after "break", remove the "else" and de-indent the code inside it (no-else-break)
weather_processor.py:157:20: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
weather_processor.py:104:31: W0613: Unused argument 'event' (unused-argument)
weather_processor.py:194:12: R1723: Unnecessary "else" after "break", remove the "else" and de-indent the code inside it (no-else-break)
weather_processor.py:165:29: W0613: Unused argument 'event' (unused-argument)
weather_processor.py:214:33: W0613: Unused argument 'event' (unused-argument)
weather_processor.py:244:34: W0613: Unused argument 'event' (unused-argument)
************* Module setup
setup.py:9:0: C0304: Final newline missing (missing-final-newline)
setup.py:1:0: C0114: Missing module docstring (missing-module-docstring)
setup.py:1:0: E0401: Unable to import 'setuptools' (import-error)
************* Module scrape_weather
scrape_weather.py:70:0: C0301: Line too long (108/100) (line-too-long)
scrape_weather.py:19:0: R0902: Too many instance attributes (13/7) (too-many-instance-attributes)
scrape_weather.py:59:24: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
scrape_weather.py:43:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
scrape_weather.py:39:4: R0912: Too many branches (15/12) (too-many-branches)
************* Module plot_operations
plot_operations.py:12:0: E0401: Unable to import 'matplotlib' (import-error)
plot_operations.py:13:0: E0401: Unable to import 'matplotlib.pyplot' (import-error)
plot_operations.py:14:0: E0401: Unable to import 'numpy' (import-error)
************* Module dist.weather_processor._internal.IPython.extensions.storemagic
dist/weather_processor/_internal/IPython/extensions/storemagic.py:236:0: C0305: Trailing newlines (trailing-newlines)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:16:0: C0410: Multiple imports on one line (inspect, os, sys, textwrap) (multiple-imports)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:18:0: E0401: Unable to import 'IPython.core.error' (import-error)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:19:0: E0401: Unable to import 'IPython.core.magic' (import-error)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:20:0: E0401: Unable to import 'IPython.testing.skipdoctest' (import-error)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:21:0: E0401: Unable to import 'traitlets' (import-error)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:24:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:43:18: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:54:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:73:8: R1725: Consider using Python 3 style super() without arguments (super-with-arguments)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:80:4: R0914: Too many local variables (25/15) (too-many-locals)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:161:12: W0622: Redefining built-in 'vars' (redefined-builtin)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:130:12: R1720: Unnecessary "else" after "raise", remove the "else" and de-indent the code inside it (no-else-raise)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:138:37: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:153:34: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:187:26: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:191:24: C0415: Import outside toplevel (pprint.pprint) (import-outside-toplevel)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:202:16: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:210:41: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:215:26: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:221:46: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:230:26: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:80:4: R0912: Too many branches (29/12) (too-many-branches)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:80:4: R0915: Too many statements (77/50) (too-many-statements)
dist/weather_processor/_internal/IPython/extensions/storemagic.py:61:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module dist.weather_processor._internal.IPython.extensions.autoreload
dist/weather_processor/_internal/IPython/extensions/autoreload.py:103:0: C0301: Line too long (138/100) (line-too-long)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:105:0: C0301: Line too long (128/100) (line-too-long)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:679:0: C0301: Line too long (102/100) (line-too-long)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:108:0: E0401: Unable to import 'IPython.core' (import-error)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:109:0: E0401: Unable to import 'IPython.core.magic' (import-error)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:144:0: C0115: Missing class docstring (missing-class-docstring)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:144:0: R0902: Too many instance attributes (11/7) (too-many-instance-attributes)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:210:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:219:8: W0612: Unused variable 'path' (unused-variable)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:271:16: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:279:16: W0702: No exception type(s) specified (bare-except)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:282:28: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:236:4: R0912: Too many branches (16/12) (too-many-branches)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:322:11: C0123: Use isinstance() rather than type() for a typecheck. (unidiomatic-typecheck)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:375:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:394:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:402:0: C0115: Missing class docstring (missing-class-docstring)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:402:0: R0903: Too few public methods (1/2) (too-few-public-methods)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:422:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:440:24: W0621: Redefining name 'reload' from outer scope (line 136) (redefined-outer-name)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:440:0: R0912: Too many branches (13/12) (too-many-branches)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:516:0: C0115: Missing class docstring (missing-class-docstring)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:635:12: W0212: Access to a protected member _report of a client class (protected-access)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:638:16: W0212: Access to a protected member _report of a client class (protected-access)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:640:16: W0212: Access to a protected member _report of a client class (protected-access)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:642:12: W0212: Access to a protected member _report of a client class (protected-access)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:646:11: R1714: Consider merging these comparisons with 'in' by using 'mode in ('', 'now')'. Use a set instead if elements are hashable. (consider-using-in)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:648:13: R1714: Consider merging these comparisons with 'in' by using 'mode in ('0', 'off')'. Use a set instead if elements are hashable. (consider-using-in)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:650:13: R1714: Consider merging these comparisons with 'in' by using 'mode in ('1', 'explicit')'. Use a set instead if elements are hashable. (consider-using-in)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:654:13: R1714: Consider merging these comparisons with 'in' by using 'mode in ('2', 'all')'. Use a set instead if elements are hashable. (consider-using-in)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:658:13: R1714: Consider merging these comparisons with 'in' by using 'mode in ('3', 'complete')'. Use a set instead if elements are hashable. (consider-using-in)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:691:29: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:692:25: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:704:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:708:12: W0702: No exception type(s) specified (bare-except)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:704:27: W0613: Unused argument 'info' (unused-argument)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:129:0: C0411: standard import "os" should be placed before third party imports "IPython.core.magic_arguments", "IPython.core.magic.Magics" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:130:0: C0411: standard import "sys" should be placed before third party imports "IPython.core.magic_arguments", "IPython.core.magic.Magics" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:131:0: C0411: standard import "traceback" should be placed before third party imports "IPython.core.magic_arguments", "IPython.core.magic.Magics" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:132:0: C0411: standard import "types" should be placed before third party imports "IPython.core.magic_arguments", "IPython.core.magic.Magics" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:133:0: C0411: standard import "weakref" should be placed before third party imports "IPython.core.magic_arguments", "IPython.core.magic.Magics" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:134:0: C0411: standard import "gc" should be placed before third party imports "IPython.core.magic_arguments", "IPython.core.magic.Magics" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:135:0: C0411: standard import "logging" should be placed before third party imports "IPython.core.magic_arguments", "IPython.core.magic.Magics" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:136:0: C0411: standard import "importlib.import_module" should be placed before third party imports "IPython.core.magic_arguments", "IPython.core.magic.Magics" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/autoreload.py:137:0: C0411: standard import "importlib.util.source_from_cache" should be placed before third party imports "IPython.core.magic_arguments", "IPython.core.magic.Magics" (wrong-import-order)
************* Module dist.weather_processor._internal.IPython.extensions.tests.test_storemagic
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:1:0: C0410: Multiple imports on one line (tempfile, os) (multiple-imports)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:4:0: E0401: Unable to import 'traitlets.config.loader' (import-error)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:8:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:11:24: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:12:24: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:13:27: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:14:27: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:15:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:16:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:17:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:18:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:20:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:21:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:22:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:23:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:26:11: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:27:20: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:28:11: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:29:11: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:32:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:33:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:34:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:35:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:36:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:37:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:40:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:41:11: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:42:11: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:43:11: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:44:11: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:46:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:47:47: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:51:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:52:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:53:4: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:54:8: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:57:18: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:59:8: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:60:8: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:61:28: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:63:8: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:64:15: E0602: Undefined variable 'ip' (undefined-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_storemagic.py:66:8: E0602: Undefined variable 'ip' (undefined-variable)
************* Module dist.weather_processor._internal.IPython.extensions.tests.test_autoreload
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:17:0: E0401: Unable to import 'pytest' (import-error)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:28:0: E0401: Unable to import 'IPython.testing.tools' (import-error)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:32:0: E0401: Unable to import 'IPython.extensions.autoreload' (import-error)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:33:0: E0401: Unable to import 'IPython.core.events' (import-error)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:34:0: E0401: Unable to import 'IPython.testing.decorators' (import-error)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:35:0: E0401: Unable to import 'IPython.core.interactiveshell' (import-error)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:47:7: C3001: Lambda expression assigned to a variable. Define a function using the "def" keyword instead. (unnecessary-lambda-assignment)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:50:0: C0115: Missing class docstring (missing-class-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:61:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:61:4: R0913: Too many arguments (6/5) (too-many-arguments)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:63:8: W0613: Unused argument 'exc_tuple' (unused-argument)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:64:8: W0613: Unused argument 'filename' (unused-argument)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:65:8: W0613: Unused argument 'tb_offset' (unused-argument)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:66:8: W0613: Unused argument 'exception_only' (unused-argument)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:67:8: W0613: Unused argument 'running_compiled_code' (unused-argument)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:71:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:82:8: W0122: Use of exec (exec-used)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:85:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:88:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:91:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:117:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:147:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:172:0: C0115: Missing class docstring (missing-class-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:173:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:199:13: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:203:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:215:28: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:239:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:257:28: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:289:27: C0208: Use a sequence type when iterating over values (use-sequence-for-iteration)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:301:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:314:28: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:331:13: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:335:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:410:22: W0612: Unused variable 'new_mod_fn' (unused-variable)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:420:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:423:8: C0115: Missing class docstring (missing-class-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:430:30: W0212: Access to a protected member _reloader of a client class (protected-access)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:447:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:449:26: W0212: Access to a protected member _reloader of a client class (protected-access)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:466:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:550:27: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:556:32: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:604:13: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:608:13: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:639:8: E0102: function already defined line 573 (function-redefined)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:678:29: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:509:4: R0915: Too many statements (78/50) (too-many-statements)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:707:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:710:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:18:0: C0411: standard import "sys" should be placed before third party import "pytest" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:19:0: C0411: standard import "tempfile" should be placed before third party import "pytest" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:20:0: C0411: standard import "textwrap" should be placed before third party import "pytest" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:21:0: C0411: standard import "shutil" should be placed before third party import "pytest" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:22:0: C0411: standard import "random" should be placed before third party import "pytest" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:23:0: C0411: standard import "time" should be placed before third party import "pytest" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:24:0: C0411: standard import "traceback" should be placed before third party import "pytest" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:25:0: C0411: standard import "io.StringIO" should be placed before third party import "pytest" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:26:0: C0411: standard import "dataclasses.dataclass" should be placed before third party import "pytest" (wrong-import-order)
dist/weather_processor/_internal/IPython/extensions/tests/test_autoreload.py:30:0: C0411: standard import "unittest.TestCase" should be placed before third party imports "pytest", "IPython.testing.tools" (wrong-import-order)
************* Module dist.weather_processor._internal.astroid.brain.brain_type
dist/weather_processor/_internal/astroid/brain/brain_type.py:66:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_numpy_core_function_base
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_function_base.py:18:0: C0301: Line too long (103/100) (line-too-long)
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_function_base.py:27:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_numpy_core_numerictypes
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_numerictypes.py:15:5: W0511: TODO: Uniformize the generic API with the ndarray one. (fixme)
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_numerictypes.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_numerictypes.py:261:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_scipy_signal
dist/weather_processor/_internal/astroid/brain/brain_scipy_signal.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_scipy_signal.py:88:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_signal
dist/weather_processor/_internal/astroid/brain/brain_signal.py:119:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_builtin_inference
dist/weather_processor/_internal/astroid/brain/brain_builtin_inference.py:1:0: C0302: Too many lines in module (1111/1000) (too-many-lines)
dist/weather_processor/_internal/astroid/brain/brain_builtin_inference.py:287:13: W0511: TODO: Does not handle deduplication for sets. (fixme)
dist/weather_processor/_internal/astroid/brain/brain_builtin_inference.py:176:8: R0916: Too many boolean expressions in if statement (8/5) (too-many-boolean-expressions)
dist/weather_processor/_internal/astroid/brain/brain_builtin_inference.py:213:0: W0613: Unused argument 'kwargs' (unused-argument)
dist/weather_processor/_internal/astroid/brain/brain_builtin_inference.py:721:26: W0613: Unused argument 'context' (unused-argument)
dist/weather_processor/_internal/astroid/brain/brain_builtin_inference.py:721:0: W0613: Unused argument 'kwargs' (unused-argument)
dist/weather_processor/_internal/astroid/brain/brain_builtin_inference.py:859:12: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/astroid/brain/brain_builtin_inference.py:918:0: R0911: Too many return statements (8/6) (too-many-return-statements)
dist/weather_processor/_internal/astroid/brain/brain_builtin_inference.py:990:0: W0613: Unused argument 'kwargs' (unused-argument)
dist/weather_processor/_internal/astroid/brain/brain_builtin_inference.py:1018:0: R0914: Too many local variables (16/15) (too-many-locals)
dist/weather_processor/_internal/astroid/brain/brain_builtin_inference.py:1019:0: W0613: Unused argument 'kwargs' (unused-argument)
dist/weather_processor/_internal/astroid/brain/brain_builtin_inference.py:1071:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_ssl
dist/weather_processor/_internal/astroid/brain/brain_ssl.py:102:0: C0301: Line too long (102/100) (line-too-long)
dist/weather_processor/_internal/astroid/brain/brain_ssl.py:49:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_ssl.py:158:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_gi
dist/weather_processor/_internal/astroid/brain/brain_gi.py:25:0: C0103: Constant name "_identifier_re" doesn't conform to UPPER_CASE naming style (invalid-name)
dist/weather_processor/_internal/astroid/brain/brain_gi.py:57:0: R0912: Too many branches (27/12) (too-many-branches)
dist/weather_processor/_internal/astroid/brain/brain_gi.py:57:0: R0915: Too many statements (62/50) (too-many-statements)
dist/weather_processor/_internal/astroid/brain/brain_gi.py:210:0: R0911: Too many return statements (7/6) (too-many-return-statements)
dist/weather_processor/_internal/astroid/brain/brain_gi.py:246:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_numpy_core_multiarray
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_multiarray.py:62:0: C0301: Line too long (107/100) (line-too-long)
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_multiarray.py:64:0: C0301: Line too long (102/100) (line-too-long)
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_multiarray.py:21:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_multiarray.py:89:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_pytest
dist/weather_processor/_internal/astroid/brain/brain_pytest.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_pytest.py:82:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_numpy_ndarray
dist/weather_processor/_internal/astroid/brain/brain_numpy_ndarray.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_numpy_ndarray.py:158:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_crypt
dist/weather_processor/_internal/astroid/brain/brain_crypt.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_crypt.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_collections
dist/weather_processor/_internal/astroid/brain/brain_collections.py:122:0: C0301: Line too long (107/100) (line-too-long)
dist/weather_processor/_internal/astroid/brain/brain_collections.py:123:0: C0301: Line too long (106/100) (line-too-long)
dist/weather_processor/_internal/astroid/brain/brain_collections.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_collections.py:109:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_collections.py:109:39: W0613: Unused argument 'context' (unused-argument)
dist/weather_processor/_internal/astroid/brain/brain_collections.py:116:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_namedtuple_enum
dist/weather_processor/_internal/astroid/brain/brain_namedtuple_enum.py:135:9: W0511: XXX this should succeed *unless* __str__/__repr__ is incorrect or throws (fixme)
dist/weather_processor/_internal/astroid/brain/brain_namedtuple_enum.py:161:5: W0511: XXX add __init__(*attributes) method (fixme)
dist/weather_processor/_internal/astroid/brain/brain_namedtuple_enum.py:74:0: R0912: Too many branches (13/12) (too-many-branches)
dist/weather_processor/_internal/astroid/brain/brain_namedtuple_enum.py:193:0: R0914: Too many local variables (16/15) (too-many-locals)
dist/weather_processor/_internal/astroid/brain/brain_namedtuple_enum.py:271:12: R0916: Too many boolean expressions in if statement (6/5) (too-many-boolean-expressions)
dist/weather_processor/_internal/astroid/brain/brain_namedtuple_enum.py:278:23: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dist/weather_processor/_internal/astroid/brain/brain_namedtuple_enum.py:388:0: R0914: Too many local variables (17/15) (too-many-locals)
dist/weather_processor/_internal/astroid/brain/brain_namedtuple_enum.py:388:0: R0912: Too many branches (20/12) (too-many-branches)
dist/weather_processor/_internal/astroid/brain/brain_namedtuple_enum.py:565:37: W0613: Unused argument 'node' (unused-argument)
dist/weather_processor/_internal/astroid/brain/brain_namedtuple_enum.py:603:0: R0912: Too many branches (13/12) (too-many-branches)
dist/weather_processor/_internal/astroid/brain/brain_namedtuple_enum.py:650:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_functools
dist/weather_processor/_internal/astroid/brain/brain_functools.py:66:5: W0511: TODO: this is not ideal, since the node should be immutable, (fixme)
dist/weather_processor/_internal/astroid/brain/brain_functools.py:35:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_functools.py:39:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_functools.py:47:8: C0115: Missing class docstring (missing-class-docstring)
dist/weather_processor/_internal/astroid/brain/brain_functools.py:60:4: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_functools.py:65:31: W0613: Unused argument 'context' (unused-argument)
dist/weather_processor/_internal/astroid/brain/brain_functools.py:162:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_regex
dist/weather_processor/_internal/astroid/brain/brain_regex.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_regex.py:73:42: W0613: Unused argument 'ctx' (unused-argument)
dist/weather_processor/_internal/astroid/brain/brain_regex.py:92:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_hypothesis
dist/weather_processor/_internal/astroid/brain/brain_hypothesis.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_six
dist/weather_processor/_internal/astroid/brain/brain_six.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_six.py:109:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_six.py:187:12: W0212: Access to a protected member _metaclass of a client class (protected-access)
dist/weather_processor/_internal/astroid/brain/brain_six.py:221:4: W0212: Access to a protected member _metaclass of a client class (protected-access)
dist/weather_processor/_internal/astroid/brain/brain_six.py:225:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_unittest
dist/weather_processor/_internal/astroid/brain/brain_unittest.py:11:0: C0103: Function name "IsolatedAsyncioTestCaseImport" doesn't conform to snake_case naming style (invalid-name)
dist/weather_processor/_internal/astroid/brain/brain_unittest.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_numpy_core_umath
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_umath.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_umath.py:152:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_pathlib
dist/weather_processor/_internal/astroid/brain/brain_pathlib.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_pathlib.py:32:23: W0212: Access to a protected member _proxied of a client class (protected-access)
dist/weather_processor/_internal/astroid/brain/brain_pathlib.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_pathlib.py:38:37: W0613: Unused argument 'ctx' (unused-argument)
dist/weather_processor/_internal/astroid/brain/brain_pathlib.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_datetime
dist/weather_processor/_internal/astroid/brain/brain_datetime.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_datetime.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_numpy_ma
dist/weather_processor/_internal/astroid/brain/brain_numpy_ma.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.helpers
dist/weather_processor/_internal/astroid/brain/helpers.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/helpers.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/helpers.py:28:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/helpers.py:28:0: R0915: Too many statements (53/50) (too-many-statements)
************* Module dist.weather_processor._internal.astroid.brain.brain_numpy_core_fromnumeric
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_fromnumeric.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_fromnumeric.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_hashlib
dist/weather_processor/_internal/astroid/brain/brain_hashlib.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_hashlib.py:96:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_dateutil
dist/weather_processor/_internal/astroid/brain/brain_dateutil.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_dateutil.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_re
dist/weather_processor/_internal/astroid/brain/brain_re.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_re.py:74:42: W0613: Unused argument 'ctx' (unused-argument)
dist/weather_processor/_internal/astroid/brain/brain_re.py:93:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_boto3
dist/weather_processor/_internal/astroid/brain/brain_boto3.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_io
dist/weather_processor/_internal/astroid/brain/brain_io.py:10:0: C0103: Constant name "TextIOWrapper" doesn't conform to UPPER_CASE naming style (invalid-name)
dist/weather_processor/_internal/astroid/brain/brain_io.py:11:0: C0103: Constant name "FileIO" doesn't conform to UPPER_CASE naming style (invalid-name)
dist/weather_processor/_internal/astroid/brain/brain_io.py:12:0: C0103: Constant name "BufferedWriter" doesn't conform to UPPER_CASE naming style (invalid-name)
dist/weather_processor/_internal/astroid/brain/brain_io.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_numpy_utils
dist/weather_processor/_internal/astroid/brain/brain_numpy_utils.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_typing
dist/weather_processor/_internal/astroid/brain/brain_typing.py:163:0: C0301: Line too long (109/100) (line-too-long)
dist/weather_processor/_internal/astroid/brain/brain_typing.py:244:9: W0511: TODO: remove _DeprecatedGenericAlias when Py3.14 min (fixme)
dist/weather_processor/_internal/astroid/brain/brain_typing.py:113:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_typing.py:188:20: W0212: Access to a protected member __cache of a client class (protected-access)
dist/weather_processor/_internal/astroid/brain/brain_typing.py:192:8: W0212: Access to a protected member _explicit_inference of a client class (protected-access)
dist/weather_processor/_internal/astroid/brain/brain_typing.py:206:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_typing.py:207:20: W0613: Unused argument 'ctx' (unused-argument)
dist/weather_processor/_internal/astroid/brain/brain_typing.py:215:23: W0613: Unused argument 'ctx' (unused-argument)
dist/weather_processor/_internal/astroid/brain/brain_typing.py:334:4: W0212: Access to a protected member _explicit_inference of a client class (protected-access)
dist/weather_processor/_internal/astroid/brain/brain_typing.py:399:4: W0212: Access to a protected member _explicit_inference of a client class (protected-access)
dist/weather_processor/_internal/astroid/brain/brain_typing.py:462:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_numpy_core_einsumfunc
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_einsumfunc.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_einsumfunc.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_http
dist/weather_processor/_internal/astroid/brain/brain_http.py:211:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_curses
dist/weather_processor/_internal/astroid/brain/brain_curses.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_curses.py:183:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_multiprocessing
dist/weather_processor/_internal/astroid/brain/brain_multiprocessing.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_multiprocessing.py:102:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_numpy_core_numeric
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_numeric.py:27:0: C0301: Line too long (109/100) (line-too-long)
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_numeric.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_numpy_core_numeric.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_subprocess
dist/weather_processor/_internal/astroid/brain/brain_subprocess.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_subprocess.py:105:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_argparse
dist/weather_processor/_internal/astroid/brain/brain_argparse.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_argparse.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_argparse.py:49:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_threading
dist/weather_processor/_internal/astroid/brain/brain_threading.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_threading.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_pkg_resources
dist/weather_processor/_internal/astroid/brain/brain_pkg_resources.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_pkg_resources.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_pkg_resources.py:70:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_uuid
dist/weather_processor/_internal/astroid/brain/brain_uuid.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_random
dist/weather_processor/_internal/astroid/brain/brain_random.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_random.py:32:19: W0212: Access to a protected member _other_fields of a client class (protected-access)
dist/weather_processor/_internal/astroid/brain/brain_random.py:33:22: W0212: Access to a protected member _astroid_fields of a client class (protected-access)
dist/weather_processor/_internal/astroid/brain/brain_random.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_random.py:100:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_fstrings
dist/weather_processor/_internal/astroid/brain/brain_fstrings.py:67:1: W0511: TODO: this fix tries to *patch* http://bugs.python.org/issue29051 (fixme)
dist/weather_processor/_internal/astroid/brain/brain_fstrings.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_fstrings.py:20:19: W0212: Access to a protected member _other_fields of a client class (protected-access)
dist/weather_processor/_internal/astroid/brain/brain_fstrings.py:21:22: W0212: Access to a protected member _astroid_fields of a client class (protected-access)
dist/weather_processor/_internal/astroid/brain/brain_fstrings.py:71:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_numpy_random_mtrand
dist/weather_processor/_internal/astroid/brain/brain_numpy_random_mtrand.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_numpy_random_mtrand.py:69:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_attrs
dist/weather_processor/_internal/astroid/brain/brain_attrs.py:94:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_qt
dist/weather_processor/_internal/astroid/brain/brain_qt.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_qt.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_qt.py:68:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_qt.py:80:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_sqlalchemy
dist/weather_processor/_internal/astroid/brain/brain_sqlalchemy.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_sqlalchemy.py:39:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_mechanize
dist/weather_processor/_internal/astroid/brain/brain_mechanize.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dist/weather_processor/_internal/astroid/brain/brain_mechanize.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_mechanize.py:123:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_nose
dist/weather_processor/_internal/astroid/brain/brain_nose.py:73:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_dataclasses
dist/weather_processor/_internal/astroid/brain/brain_dataclasses.py:355:0: W0012: Unknown option value for 'disable-next', expected a valid pylint message and got 'else-if-used' (unknown-option-value)
dist/weather_processor/_internal/astroid/brain/brain_dataclasses.py:186:13: W0511: # TODO: This should return an Uninferable as this would raise (fixme)
dist/weather_processor/_internal/astroid/brain/brain_dataclasses.py:182:28: W0212: Access to a protected member _get_arguments_data of a client class (protected-access)
dist/weather_processor/_internal/astroid/brain/brain_dataclasses.py:241:0: R0912: Too many branches (37/12) (too-many-branches)
dist/weather_processor/_internal/astroid/brain/brain_dataclasses.py:241:0: R0915: Too many statements (90/50) (too-many-statements)
dist/weather_processor/_internal/astroid/brain/brain_dataclasses.py:620:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_ctypes
dist/weather_processor/_internal/astroid/brain/brain_ctypes.py:27:0: C0301: Line too long (101/100) (line-too-long)
dist/weather_processor/_internal/astroid/brain/brain_ctypes.py:82:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module dist.weather_processor._internal.astroid.brain.brain_responses
dist/weather_processor/_internal/astroid/brain/brain_responses.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_responses.py:78:0: C0116: Missing function or method docstring (missing-function-docstring)
dist/weather_processor/_internal/astroid/brain/brain_responses.py:1:0: R0801: Similar lines in 2 files
==dist.weather_processor._internal.astroid.brain.brain_re:[64:93]
==dist.weather_processor._internal.astroid.brain.brain_regex:[63:92]
        and isinstance(node.func, nodes.Name)
        and node.func.name == "type"
        and isinstance(node.parent, nodes.Assign)
        and len(node.parent.targets) == 1
        and isinstance(node.parent.targets[0], nodes.AssignName)
        and node.parent.targets[0].name in {"Pattern", "Match"}
    )


def infer_pattern_match(node: nodes.Call, ctx: context.InferenceContext | None = None):
    """Infer regex.Pattern and regex.Match as classes.

    For PY39+ add `__class_getitem__`.
    """
    class_def = nodes.ClassDef(
        name=node.parent.targets[0].name,
        lineno=node.lineno,
        col_offset=node.col_offset,
        parent=node.parent,
        end_lineno=node.end_lineno,
        end_col_offset=node.end_col_offset,
    )
    if PY39_PLUS:
        func_to_add = _extract_single_node(CLASS_GETITEM_TEMPLATE)
        class_def.locals["__class_getitem__"] = [func_to_add]
    return iter([class_def])


def register(manager: AstroidManager) -> None: (duplicate-code)
dist/weather_processor/_internal/astroid/brain/brain_responses.py:1:0: R0801: Similar lines in 2 files
==dist.weather_processor._internal.astroid.brain.brain_fstrings:[18:33]
==dist.weather_processor._internal.astroid.brain.brain_random:[30:45]
    cls = node.__class__
    other_fields = node._other_fields
    _astroid_fields = node._astroid_fields
    init_params = {
        "lineno": lineno,
        "col_offset": node.col_offset,
        "parent": parent,
        "end_lineno": node.end_lineno,
        "end_col_offset": node.end_col_offset,
    }
    postinit_params = {param: getattr(node, param) for param in _astroid_fields}
    if other_fields:
        init_params.update({param: getattr(node, param) for param in other_fields})
    new_node = cls(**init_params)
    if hasattr(node, "postinit") and _astroid_fields: (duplicate-code)
dist/weather_processor/_internal/astroid/brain/brain_responses.py:1:0: R0801: Similar lines in 2 files
==dist.weather_processor._internal.astroid.brain.brain_numpy_core_multiarray:[91:100]
==dist.weather_processor._internal.astroid.brain.brain_numpy_core_numeric:[40:49]
    )

    for method_name, function_src in METHODS_TO_BE_INFERRED.items():
        inference_function = functools.partial(infer_numpy_member, function_src)
        manager.register_transform(
            Attribute,
            inference_tip(inference_function),
            functools.partial(attribute_looks_like_numpy_member, method_name),
        ) (duplicate-code)
dist/weather_processor/_internal/astroid/brain/brain_responses.py:1:0: R0801: Similar lines in 2 files
==dist.weather_processor._internal.astroid.brain.brain_builtin_inference:[709:715]
==dist.weather_processor._internal.astroid.brain.brain_typing:[219:225]
        lineno=node.lineno,
        col_offset=node.col_offset,
        parent=node.parent,
        end_lineno=node.end_lineno,
        end_col_offset=node.end_col_offset,
    ) (duplicate-code)
dist/weather_processor/_internal/astroid/brain/brain_responses.py:1:0: R0801: Similar lines in 2 files
==dist.weather_processor._internal.astroid.brain.brain_builtin_inference:[426:432]
==dist.weather_processor._internal.astroid.brain.brain_re:[80:86]
            lineno=node.lineno,
            col_offset=node.col_offset,
            parent=node.parent,
            end_lineno=node.end_lineno,
            end_col_offset=node.end_col_offset,
        ) (duplicate-code)
dist/weather_processor/_internal/astroid/brain/brain_responses.py:1:0: R0801: Similar lines in 2 files
==dist.weather_processor._internal.astroid.brain.brain_builtin_inference:[246:252]
==dist.weather_processor._internal.astroid.brain.brain_regex:[79:85]
            lineno=node.lineno,
            col_offset=node.col_offset,
            parent=node.parent,
            end_lineno=node.end_lineno,
            end_col_offset=node.end_col_offset,
        ) (duplicate-code)
dist/weather_processor/_internal/astroid/brain/brain_responses.py:1:0: R0801: Similar lines in 2 files
==dist.weather_processor._internal.astroid.brain.brain_builtin_inference:[177:183]
==dist.weather_processor._internal.astroid.brain.brain_regex:[63:69]
        and isinstance(node.func, nodes.Name)
        and node.func.name == "type"
        and isinstance(node.parent, nodes.Assign)
        and len(node.parent.targets) == 1
        and isinstance(node.parent.targets[0], nodes.AssignName)
        and node.parent.targets[0].name in {"Pattern", "Match"} (duplicate-code)

-----------------------------------
Your code has been rated at 8.23/10

