class edit_distance:

#--------------------- Class variables --------------------------------------------#
    MATCH = 0
    INSERT = 1
    DELETE = 2
    REPLACE = 3
    output = ""

#------------------------------------------------------------------------------------

#--------------------- To reconstruct the path of edit distance to find out the operations done -------------

    def reconstruct_path(self,s,t,i,j,output):
        if(m[i][j]["parent"] == -1):
            return

        if(m[i][j]["parent"] == self.MATCH):
            self.reconstruct_path(s,t,str(int(i)-1),str(int(j)-1),output)
            self.output += "M "
            return

        if(m[i][j]["parent"] == self.REPLACE):
            self.reconstruct_path(s,t,str(int(i)-1),str(int(j)-1),output)
            self.output += "R("+s[int(i)]+")("+t[int(j)]+") "
            return

        if(m[i][j]["parent"] == self.INSERT):
            self.reconstruct_path(s,t,str(int(i)),str(int(j)-1),output)
            self.output += "I("+t[int(j)]+") "
            return

        if(m[i][j]["parent"] == self.DELETE):
            self.reconstruct_path(s,t,str(int(i)-1),str(int(j)),output)
            self.output += "D("+s[int(i)]+") "
            return

#---------------------------------------------------------------------------------------------------------------

    def match(self,s,t):
        if(s==t):
            return 0
        else:
            return 1

#------------------------------------- Edit distance Algorithm --------------------------------------------------

    def string_compare(self,s,t):
        global m
        m = {}
        for i in range(0,102):
            m[str(i)]={}
            for j in range(0,102):
                m[str(i)][str(j)]={}
                m[str(i)][str(j)]["cost"] = 0
                m[str(i)][str(j)]["parent"] = -1


        opt=[0,0,0]
        for i in range(1,len(s)):
            for j in range(1,len(t)):
                ms = self.match(s[i],t[j])
                match_value = m[str(i-1)][str(j-1)]["cost"] + ms
                opt[self.INSERT] = m[str(i)][str(j-1)]["cost"] + 1
                opt[self.DELETE] = m[str(i-1)][str(j)]["cost"] + 1

                m[str(i)][str(j)]["cost"] = match_value
                if(ms):
                    m[str(i)][str(j)]["parent"] = self.REPLACE
                else:
                    m[str(i)][str(j)]["parent"] = self.MATCH

                for k in range(self.INSERT,self.DELETE+1):
                    if(opt[k] < m[str(i)][str(j)]["cost"]):
                        m[str(i)][str(j)]["cost"] = opt[k]
                        m[str(i)][str(j)]["parent"] = k

        self.reconstruct_path(s,t,str(len(s)-1),str(len(t)-1),"")

#---------------------------------------------------------------------------------------------------------------------
