import re

nucValidation = re.compile(r"[A-Za-z]{3}\/[A-Za-z]{3}\/[A-Za-z]{3}\/[1-9][0-9]{3}\/[0-9]{3}\/[0-9]{4,5}")
noControlValidation = re.compile(r"[0-9]{3}\/[1-9][0-9]{3}")
noOficioValidation = re.compile(r"OF [0-9]{3}\/[1-9][0-9]{3}")
nombresValidation = re.compile(r"[^,]+")