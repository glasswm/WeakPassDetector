import os
import dboperator as dbo

def isWeak(md5Str):
    rainTableName = "md5_numeric#1-8_0_300x4000000_oxid#000.rt"
    cmd = "rcrack.exe " + rainTableName + " -h " + md5Str + " | find \"plaintext of\""
    
    result = os.popen(cmd).readlines()
    if len(result) > 0:
        dbo.updateTable(md5Str, "weakmd5")
        return True
    else:
        dbo.updateTable(md5Str, "strongmd5")
        return False
    
if __name__ == "__main__":
    print(isWeak("d3d9446802a44259755d38e6d163e820"))
    dbo.showTable("weakmd5")
#    dbo.showTable("strongmd5")