#!/usr/bin/python
#-*- coding: utf-8 -*-

import MySQLdb
import sys
import os.path
from xml.etree import cElementTree as ET
import Tkinter, Tkconstants, tkFileDialog, tkMessageBox
from ScrolledText import ScrolledText
from Tkinter import *

class Delete:               #allows for deletion of words
    global whichTbl
    def delete(self, cur, name, lesson, exercise, appearance, bFrame, t):
        #sqlq = "SELECT COUNT(1) FROM table1 WHERE Name = 'hi'"
        #cur.execute(sqlq)
        #print cur.fetchone()[0]
         #   print "found it"
        n = name.get()
        l = lesson.get()
        e = exercise.get()
        a = appearance.get()
        if whichTbl == 1:
            if n and l and e and a:                                             #if all columns have data
                statement = "DELETE FROM table1 WHERE Name LIKE %s AND Lesson LIKE %s AND Exercise LIKE %s AND Appearance LIKE %s"
                cur.execute(statement, (n, l, e, a))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n and l and e:                                             #name, lesson, and exercise
                statement = "DELETE FROM table1 WHERE Name LIKE %s AND Lesson LIKE %s AND Exercise LIKE %s"
                cur.execute(statement, (n, l, e))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n and l and a:                                                   #name, lesson and appearance
                statement = "DELETE FROM table1 WHERE Name LIKE %s AND Lesson LIKE %s AND Appearance LIKE %s"
                cur.execute(statement, (n, l, a))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n and e and a:
                statement = "DELETE FROM table1 WHERE Name LIKE %s AND Exercise LIKE %s AND Appearance"
                cur.execute(statement, (n, e, a))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif l and e and a:                                                   #lesson, exercise and appearance
                statement = "DELETE FROM table1 WHERE Lesson LIKE %s AND Exercise LIKE %s AND Appearance LIKE %s"
                cur.execute(statement, (l, e, a))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n and l:                                                   #name and lesson
                statement = "DELETE FROM table1 WHERE Name LIKE %s AND Lesson LIKE %s"
                cur.execute(statement, (n, l))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n and a:
                statement = "DELETE FROM table1 WHERE Name LIKE %s AND Appearance LIKE %s"
                cur.execute(statement, (n, a))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n and e:                                                   #name and exercise
                statement = "DELETE FROM table1 WHERE Name LIKE %s AND Exercise LIKE %s"
                cur.execute(statement, (n, e))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif l and e:                                                   #lesson and exercise
                statement = "DELETE FROM table1 WHERE Lesson LIKE %s AND Exercise LIKE %s"
                cur.execute(statement, (l, e))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif l and a:                                                   #lesson and appearance
                statement = "DELETE FROM table1 WHERE Lesson LIKE %s AND Appearance LIKE %s"
                cur.execute(statement, (l, a))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n:                                                         #name
                statement = "DELETE FROM table1 WHERE Name LIKE %s"
                cur.execute(statement, (n))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif l:                                                         #lesson
                statement = "DELETE FROM table1 WHERE Lesson LIKE %s"
                cur.execute(statement, (l))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif e:                                                         #exercise
                statement = "DELETE FROM table1 WHERE Exercise LIKE %s"
                cur.execute(statement, (e))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif a:                                                         #appearance
                statement = "DELETE FROM table1 WHERE Exercise LIKE %s"
                cur.execute(statement, (e))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
        elif whichTbl == 2:
            if n and l and e and a:                                             #if all columns have data
                statement = "DELETE FROM table2 WHERE Name LIKE %s AND Lesson LIKE %s AND Exercise LIKE %s AND Appearance LIKE %s"
                cur.execute(statement, (n, l, e, a))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n and l and e:                                             #name, lesson, and exercise
                statement = "DELETE FROM table2 WHERE Name LIKE %s AND Lesson LIKE %s AND Exercise LIKE %s"
                cur.execute(statement, (n, l, e))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n and l and a:                                                   #name, lesson and appearance
                statement = "DELETE FROM table2 WHERE Name LIKE %s AND Lesson LIKE %s AND Appearance LIKE %s"
                cur.execute(statement, (n, l, a))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n and e and a:
                statement = "DELETE FROM table2 WHERE Name LIKE %s AND Exercise LIKE %s AND Appearance"
                cur.execute(statement, (n, e, a))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif l and e and a:                                                   #lesson, exercise and appearance
                statement = "DELETE FROM table2 WHERE Lesson LIKE %s AND Exercise LIKE %s AND Appearance LIKE %s"
                cur.execute(statement, (l, e, a))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n and l:                                                          #name and lesson
                statement = "DELETE FROM table2 WHERE Name LIKE %s AND Lesson LIKE %s"
                cur.execute(statement, (n, l))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n and a:
                statement = "DELETE FROM table2 WHERE Name LIKE %s AND Appearance LIKE %s"
                cur.execute(statement, (n, a))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n and e:                                                   #name and exercise
                statement = "DELETE FROM table2 WHERE Name LIKE %s AND Exercise LIKE %s"
                cur.execute(statement, (n, e))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif l and e:                                                   #lesson and exercise
                statement = "DELETE FROM table2 WHERE Lesson LIKE %s AND Exercise LIKE %s"
                cur.execute(statement, (l, e))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif l and a:                                                   #lesson and appearance
                statement = "DELETE FROM table2 WHERE Lesson LIKE %s AND Appearance LIKE %s"
                cur.execute(statement, (l, a))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif n:                                                         #name
                statement = "DELETE FROM table2 WHERE Name LIKE %s"
                cur.execute(statement, (n))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif l:                                                         #lesson
                statement = "DELETE FROM table2 WHERE Lesson LIKE %s"
                cur.execute(statement, (l))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif e:                                                         #exercise
                statement = "DELETE FROM table2 WHERE Exercise LIKE %s"
                cur.execute(statement, (e))
                bFrame.printBottom(t, cur, 0, '', '', '', '')
            elif a:                                                         #appearance
                statement = "DELETE FROM table2 WHERE Exercise LIKE %s"
                cur.execute(statement, (e))
                bFrame.printBottom(t, cur, 0, '', '', '', '')

class Left:                #includes name, lesson, exercise, and browse events. Allows user to enter information manually or upload documents from computer.
    def handleAdd(self, name, lesson, exercise, appearance, cur, bFrame, t):
        global whichTbl
        
        print "add"
        n = name.get()
        l = lesson.get()
        e = exercise.get()
        a = appearance.get()


        #---------------------MySQL
        if whichTbl == 1:
            cur.execute("INSERT INTO table1(Name, Lesson, Exercise, Appearance) VALUES('%s', '%s', '%s', '%s')" %(n, l, e, a))     #put values into table, one row at a time
        elif whichTbl == 2:
            cur.execute("INSERT INTO table2(Name, Lesson, Exercise, Appearance) VALUES('%s', '%s', '%s', '%s')" %(n, l, e, a))     #put values into table, one row at a time
        #--------------------------
        bFrame.printBottom(t, cur, 0, '', '', '', '')
    def handleDelete(self, name, lesson, exercise, appearance, cur, bFrame, t):
        print "delete"
        dele = Delete()                  #new instance of class delete
        dele.delete(cur, name, lesson, exercise, appearance, bFrame, t)

    def leftFrame(self, t, cur):
        #instantiate bottom-------------------------------------------------------------------
        bFrame = Bottom()
        bFrame.bottomFrame(t, cur)
        #-------------------------------------------------------------------------------------
        manEnterLabel = Tkinter.Label(t, text = "Manual/loaded entries").grid(row = 0, column = 0)
    
        manNamel = Tkinter.Label(t, text = "name").grid(row = 1, column = 0)
        manLessl = Tkinter.Label(t, text = "lesson").grid(row = 2, column = 0)
        manExerl = Tkinter.Label(t, text = "exercise").grid(row = 3, column = 0)
        manExerl = Tkinter.Label(t, text = "appearance").grid(row = 4, column = 0)

        vN = StringVar()                                    #to change name field into string literal
        vL = StringVar()                                    #to change lesson field into string literal
        vE = StringVar()                                    #to change exercise field into string literal
        vA = StringVar()                                    #to change appearance field into string literal
        manName = Tkinter.Entry(t, textvariable = vN).grid(row = 1, column = 1, columnspan = 2)
        manLess = Tkinter.Entry(t, textvariable = vL).grid(row = 2, column = 1, columnspan = 2)
        manExer = Tkinter.Entry(t, textvariable = vE).grid(row = 3, column = 1, columnspan = 2)
        manExer = Tkinter.Entry(t, textvariable = vA).grid(row = 4, column = 1, columnspan = 2)
        manEnter = Tkinter.Button(t, text = "add", command = lambda : self.handleAdd(vN, vL, vE, vA, cur, bFrame, t))
        manEnter.grid(row = 5, column = 1)
        manEnter = Tkinter.Button(t, text = "delete", command = lambda : self.handleDelete(vN, vL, vE, vA, cur, bFrame, t))
        manEnter.grid(row = 5, column = 2)
        

        rFrame = Right()
        rFrame.rightFrame(t, cur, bFrame)


class Right:                #includes 4 substring fields; lesson, exercise, and name selections; a menu of logical symbols; and a text field to enter logical strings
    def handleEnterLog(self, t, cur, bFrame, strings, name, lesson, exercise):
        s = strings.get()
        n = name.get()
        l = lesson.get()
        e = exercise.get()
        print n
        bFrame.printBottom(t, cur, 1, s, n, l, e)
        #global whichTbl
        #if whichTbl == 1:
         #   cur.execute("SELECT * FROM table1")         #select all data from table
        #elif whichTbl == 2:
         #   cur.execute("SELECT * FROM table2")         #select all data from table
    def handleStr(self, num):
        print num
    def rightFrame(self, t, cur, bFrame):
        vN = StringVar()                                #to change str field into string literal
        vN1 = StringVar()
        vN2 = StringVar()
        vN3 = StringVar()

        name = StringVar()                              #to change name field into string literal
        lesson = StringVar()
        exercise = StringVar()
        
        ent1 = Tkinter.Entry(t, textvariable = vN).grid(row = 1, column = 12)
        ent2 = Tkinter.Entry(t, textvariable = vN1).grid(row = 2, column = 12)
        ent3 = Tkinter.Entry(t, textvariable = vN2).grid(row = 3, column = 12)
        ent4 = Tkinter.Entry(t, textvariable = vN3).grid(row = 4, column = 12)
        ent2 = Tkinter.Entry(t, textvariable = name).grid(row = 5, column = 12)
        ent3 = Tkinter.Entry(t, textvariable = lesson).grid(row = 6, column = 12)
        ent4 = Tkinter.Entry(t, textvariable = exercise).grid(row = 7, column = 12)
        
        str1 = Tkinter.Button(t, text = "str1", command = lambda : self.handleStr(1))
        str1.grid(row = 1, column = 11)
        str2 = Tkinter.Button(t, text = "str2", command = lambda : self.handleStr(2))
        str2.grid(row = 2, column = 11)
        str3 = Tkinter.Button(t, text = "str3", command = lambda : self.handleStr(3))
        str3.grid(row = 3, column = 11)
        str4 = Tkinter.Button(t, text = "str4", command = lambda : self.handleStr(4))
        str4.grid(row = 4, column = 11)
        nStr = Tkinter.Button(t, text = "Name", command = lambda : self.handleStr(4))
        nStr.grid(row = 5, column = 11)
        lStr = Tkinter.Button(t, text = "Lesson", command = lambda : self.handleStr(4))
        lStr.grid(row = 6, column = 11)
        eStr = Tkinter.Button(t, text = "Exercise", command = lambda : self.handleStr(4))
        eStr.grid(row = 7, column = 11)
        strings = vN                           #determine the string to be used
        enter = Tkinter.Button(t, text = "enter logic", command = lambda : self.handleEnterLog(t, cur, bFrame, strings, name, lesson, exercise))
        enter.grid(row = 8, column = 12)

        logLabel = Tkinter.Label(t, text = "Logical Statements").grid(row = 0, column = 13)
        logicWind = Tkinter.Text(t, width = 45, height = 15).grid(columnspan = 10, rowspan = 10, row = 1, column = 13)
 

class Bottom:              #includes a large text field for displaying lists

    listDisp = Tkinter
    sort = Tkinter
    def bottomFrame(self, t, cur):
        mFrame = Menus()                                    #for menu
        Bottom.sort = IntVar()
        sortLabel = Tkinter.Label(t, text = "Sort by ").grid(row = 11, column = 4)
        Bottom.sortByName = Tkinter.Radiobutton(t, text = "Name", variable = Bottom.sort, value = 1).grid(row = 11, column = 6)
        Bottom.sortByExercise = Tkinter.Radiobutton(t, text = "Exercise", variable = Bottom.sort, value = 2).grid(row = 11, column = 7)
        Bottom.sortByLesson = Tkinter.Radiobutton(t, text = "Lesson", variable = Bottom.sort, value = 3).grid(row = 11, column = 8)
        Bottom.sortByAppearance = Tkinter.Radiobutton(t, text = "Appearance", variable = Bottom.sort, value = 4).grid(row = 11, column = 9)
        mFrame.menuFrame(t, cur, Bottom.sort, self)                          #for menu
        Bottom.listDisp = ScrolledText(t, width = 75, height = 25)
        Bottom.listDisp.grid(columnspan = 20, rowspan = 20, row = 12, column = 0)

        tab = Tables()
        tab.createTable(t, cur)
        tab.showTables(t, cur)


    def printBottom(self, t, cur, logic, s, n, l, e):                       #'logic' is a boolean value
        global whichTbl
        tableName = ""
        print str(Bottom.sort.get())
        Bottom.listDisp.delete("1.0", END)
        #mysql---------------------------------------------------------------------------------------------------------
        if whichTbl == 1:
            tableName = "table1"
            if str(logic) == '1':                                   #if wanted to sort by logic
                if s and n and l and e:                             #if specified by logical string, name, lesson, and exercise
                    statement = "SELECT * FROM table1 WHERE Name LIKE %s AND Lesson LIKE %s AND Exercise LIKE %s"
                    cur.execute(statement, (n, l, e))
                elif s and n and l:
                    statement = "SELECT * FROM table1 WHERE Name LIKE %s AND Lesson LIKE %s"
                    cur.execute(statement, (n, l))
                elif s and n and e:
                    statement = "SELECT * FROM table1 WHERE Name LIKE %s AND Exercise LIKE %s"
                    cur.execute(statement, (n, e))
                elif s and l and e:
                    statement = "SELECT * FROM table1 WHERE Lesson LIKE %s AND Exercise LIKE %s"
                    cur.execute(statement, (l, e))
                elif s and n:
                    statement = "SELECT * FROM table1 WHERE Name LIKE %s"
                    cur.execute(statement, (n))
                elif s and l:
                    statement = "SELECT * FROM table1 WHERE Lesson LIKE %s"
                    cur.execute(statement, (l))
                elif s and e:
                    statement = "SELECT * FROM table1 WHERE Exercise LIKE %s"
                    cur.execute(statement, (e))
                elif n and l and e:
                    statement = "SELECT * FROM table1 WHERE Name LIKE %s AND Lesson LIKE %s AND Exercise LIKE %s"
                    cur.execute(statement, (n, l, e))
                elif n and l:
                    statement = "SELECT * FROM table1 WHERE Name LIKE %s AND Lesson LIKE %s"
                    cur.execute(statement, (n, l))
                elif n and e:
                    statement = "SELECT * FROM table1 WHERE Name LIKE %s AND Exercise LIKE %s"
                    cur.execute(statement, (n, e))
                elif l and e:
                    statement = "SELECT * FROM table1 WHERE Lesson LIKE %s AND Exercise LIKE %s"
                    cur.execute(statement, (l, e))
                elif s:
                    print "not done yet"
                elif n:
                    statement = "SELECT * FROM table1 WHERE Name LIKE %s"
                    cur.execute(statement, (n))
                elif l:
                    statement = "SELECT * FROM table1 WHERE Lesson LIKE %s"
                    cur.execute(statement, (l))
                elif e:
                    statement = "SELECT * FROM table1 WHERE Exercise LIKE %s"
                    cur.execute(statement, (e))
                    
            elif str(Bottom.sort.get()) == '1':
                cur.execute("SELECT * FROM table1 ORDER BY Name")    #get all data from table by name
            elif str(Bottom.sort.get()) == '2':
                cur.execute("SELECT *, CAST(SUBSTRING_INDEX(Exercise, '-', -1) AS UNSIGNED) as num FROM table1 ORDER BY num")      #get all data from table by exercise
            elif str(Bottom.sort.get()) == '3':
                cur.execute("SELECT *, CAST(SUBSTRING_INDEX(Lesson, '-', -1) AS UNSIGNED) as num FROM table1 ORDER BY num")      #get all data from table by lesson
            elif str(Bottom.sort.get()) == '4':
                cur.execute("SELECT *, CAST(SUBSTRING_INDEX(Appearance, '-', -1) AS UNSIGNED) as num FROM table1 ORDER BY num")      #get all data from table by appearance
            else:                                                       #nothing selected
                cur.execute("SELECT * FROM table1")                    #get everything with no particular order
        elif whichTbl == 2:
            tableName = "table2"
            if str(logic) == '1':                                   #if wanted to sort by logic
                if s and n and l and e:                             #if specified by logical string, name, lesson, and exercise
                    statement = "SELECT * FROM table2 WHERE Name LIKE %s AND Lesson LIKE %s AND Exercise LIKE %s"
                    cur.execute(statement, (n, l, e))
                elif s and n and l:
                    statement = "SELECT * FROM table2 WHERE Name LIKE %s AND Lesson LIKE %s"
                    cur.execute(statement, (n, l))
                elif s and n and e:
                    statement = "SELECT * FROM table2 WHERE Name LIKE %s AND Exercise LIKE %s"
                    cur.execute(statement, (n, e))
                elif s and l and e:
                    statement = "SELECT * FROM table2 WHERE Lesson LIKE %s AND Exercise LIKE %s"
                    cur.execute(statement, (l, e))
                elif s and n:
                    statement = "SELECT * FROM table2 WHERE Name LIKE %s"
                    cur.execute(statement, (n))
                elif s and l:
                    statement = "SELECT * FROM table2 WHERE Lesson LIKE %s"
                    cur.execute(statement, (l))
                elif s and e:
                    statement = "SELECT * FROM table2 WHERE Exercise LIKE %s"
                    cur.execute(statement, (e))
                elif n and l and e:
                    statement = "SELECT * FROM table2 WHERE Name LIKE %s AND Lesson LIKE %s AND Exercise LIKE %s"
                    cur.execute(statement, (n, l, e))
                elif n and l:
                    statement = "SELECT * FROM table2 WHERE Name LIKE %s AND Lesson LIKE %s"
                    cur.execute(statement, (n, l))
                elif n and e:
                    statement = "SELECT * FROM table2 WHERE Name LIKE %s AND Exercise LIKE %s"
                    cur.execute(statement, (n, e))
                elif l and e:
                    statement = "SELECT * FROM table2 WHERE Lesson LIKE %s AND Exercise LIKE %s"
                    cur.execute(statement, (l, e))
                elif s:
                    print "not done yet"
                elif n:
                    statement = "SELECT * FROM table2 WHERE Name LIKE %s"
                    cur.execute(statement, (n))
                elif l:
                    statement = "SELECT * FROM table2 WHERE Lesson LIKE %s"
                    cur.execute(statement, (l))
                elif e:
                    statement = "SELECT * FROM table2 WHERE Exercise LIKE %s"
                    cur.execute(statement, (e))
            elif str(Bottom.sort.get()) == '1':
                cur.execute("SELECT * FROM table2 ORDER BY Name")    #get all data from table by name
            elif str(Bottom.sort.get()) == '2':
                cur.execute("SELECT *, CAST(SUBSTRING_INDEX(Exercise, '-', -1) AS UNSIGNED) as num FROM table2 ORDER BY num")      #get all data from table by exercise
            elif str(Bottom.sort.get()) == '3':
                cur.execute("SELECT *, CAST(SUBSTRING_INDEX(Lesson, '-', -1) AS UNSIGNED) as num FROM table2 ORDER BY num")      #get all data from table by lesson
            elif str(Bottom.sort.get()) == '4':
                cur.execute("SELECT *, CAST(SUBSTRING_INDEX(Appearance, '-', -1) AS UNSIGNED) as num FROM table2 ORDER BY num")      #get all data from table by appearance
            else:                                                       #nothing selected
                cur.execute("SELECT * FROM table2")                    #get everything with no particular order
        desc = cur.description                  #get 'met data' (column titles)
        rows = cur.fetchall()           #get all records (in the table)
        Bottom.listDisp.insert(END, "Table: " + tableName + "\n")
        Bottom.listDisp.insert(END, desc[0][0] + desc[1][0] + desc[2][0] + desc[3][0])
        for row in rows:                #for each row
            #print row["Name"], row["Lesson"], row["Exercise"], row["Appearance"]
            Bottom.listDisp.insert(END, "\n" + row["Name"] + "\t" + row["Lesson"] + "\t" + row["Exercise"] + "\t" + row["Appearance"])
        #-------------------------------------------------------------------------------------------------------------
    

class Menus:                 #includes file menu with save; lesson, exercise, and name options for sorting
    openFile = ""           #this will contain the name of the file to be saved
    def menuFrame(self, t, cur, bSort, s):
        menuBar = Tkinter.Menu(t)
        t.config(menu = menuBar)

        #file----------------------------------------------------
        file = Tkinter.Menu(menuBar, tearoff = 0)
        file.add_command(label = "Merge", command = lambda : self.handleMerge(t, bSort, cur, s))
        file.add_command(label = "Open", command = lambda : self.handleOpen(t, bSort, cur, s))
        file.add_command(label = "Save", command = lambda : self.handleSave(bSort, cur))
        file.add_command(label = "Save as...", command = lambda : self.handleSaveAs(bSort, cur))
        file.add_command(label = "Close", command = self.handleClose)
        file.add_separator()
        file.add_command(label = "Exit", command = t.quit)
        menuBar.add_cascade(label="File", menu = file)
        #symbols--------------------------------------------------
        symbols = Tkinter.Menu(menuBar, tearoff = 0)
        symbols.add_command(label = "And", command = self.handleAnd)
        symbols.add_command(label = "Or", command = self.handleOr)
        symbols.add_command(label = "Not", command = self.handleNot)
        #edit-----------------------------------------------------
        edit = Tkinter.Menu(menuBar, tearoff = 0)
        edit.add_command(label = "Undo", command = self.handleUndo)
        edit.add_command(label = "Redo", command = self.handleRedo)

        menuBar.add_cascade(label = "Edit", menu = edit)
        menuBar.add_cascade(label= "Symbols", menu = symbols)

        #define options for opening or saving a file
        self.fOptions = options = {}
        options['defaultextension'] = '.txt'
        options['parent'] = t
        options['initialdir'] = 'C:\\'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt'), ('spreadsheet or open-office', '.odt'), ('xml', '.xml')]
    
    
    #file------------------------------------     
    def handleMerge(self, t, bSort, cur, s):                            #allows the merging of tables
        global whichTbl
        print("Merge")
        self.fileName = tkFileDialog.askopenfilename(**self.fOptions)    #open dialogue window options specified above which reutrns file name
        #if file by specified name exists
        if self.fileName:
            print "File found"
            #put lines of file into array called fileLines
            f = open(self.fileName, "r")            #open specified for reading
            extension = os.path.splitext(self.fileName)[1]  #get file extension
            print extension                         
            array = []                              #create 1-dimensional array to store individual lines
            wordArray = []                          #create 1-dimensional array to store individual words
            if extension == ".txt":
                for i in f:                             #for each line in file
                    array.append( i )                   #put line in array
                for lines in array:                     #for each element of array
                    wordArray.append(lines.split())     #create array with just words         
                for i in wordArray[::1]:                #for each element of wordArray
                    #mysql---------------------------------------------------------------
                    if whichTbl == 1:
                        print len(i)
                        if len(i) == 4:
                            cur.execute("INSERT INTO table1(Name, Lesson, Exercise, Appearance) VALUES('%s', '%s', '%s', '%s')" %(i[0], i[1], i[2], i[3]))     #put values into table, one row at a time
                        else:
                            tkMessageBox.showwarning("Wrong format", "The file you are trying to merge does not have the correct number of fields (4)")                        
                    elif whichTbl == 2:
                        if len(i) == 4:
                            cur.execute("INSERT INTO table2(Name, Lesson, Exercise, Appearance) VALUES('%s', '%s', '%s', '%s')" %(i[0], i[1], i[2], i[3]))     #put values into table, one row at a time
                        else:
                            tkMessageBox.showwarning("Wrong format", "The file you are trying to merge does not have the correct number of fields (4)")
                    #--------------------------------------------------------------------
            elif extension == ".xml":
                print "file xml"
                for i in f:
                    content = i.find('w:t').text
                    print content
            f.close()
            s.printBottom(t, cur, 0, '', '', '', '')
    def handleOpen(self, t, bSort, cur, s):                         #does the exact same thing as handleMerge, only it clears the table first
        global whichTbl
        yesNo = tkMessageBox.askokcancel("Open", "If you open, all data will be replaced in current table. To add contents of file to table, select file->merge")
        if yesNo:
            #mysql----------------------------------------------------------
            if whichTbl == 1:
                cur.execute("TRUNCATE TABLE table1")                      #delete contents of table
            elif whichTbl == 2:
                cur.execute("TRUNCATE TABLE table2")                    #delte contents of table 
            #---------------------------------------------------------------
            self.handleMerge(t, bSort, cur, s)
    def handleSaveAs2(self, bSort, cur):                            #returns open file whose name is specified
        print "Save as"
        return tkFileDialog.asksaveasfilename(**self.fOptions)                #open dialogue window using options specified above
    def handleSaveAs(self, bSort, cur):                             #saves content of text box to specified file
        self.openFile = self.handleSaveAs2(bSort, cur)
        self.handleSave(bSort, cur)
    def handleSave(self, bSort, cur):                     #openFile must exist in order for this function to work
        global whichTbl
        if self.openFile == "":                              #if file doesn't exist
            tkMessageBox.showinfo("Annoying message", "Sorry. You must first select a file name using 'file->save as.'")
        else:
            if whichTbl == 1:
                if str(bSort.get()) == '1':
                    cur.execute("SELECT * FROM table1 ORDER BY Name")    #get all data from table by name
                elif str(bSort.get()) == '2':
                    cur.execute("SELECT *, CAST(SUBSTRING_INDEX(Exercise, '-', -1) AS UNSIGNED) as num FROM table1 ORDER BY num")      #get all data from table by exercise
                elif str(bSort.get()) == '3':
                    cur.execute("SELECT *, CAST(SUBSTRING_INDEX(Lesson, '-', -1) AS UNSIGNED) as num FROM table1 ORDER BY num")      #get all data from table by lesson
                else:
                    cur.execute("SELECT * FROM table1")
            elif whichTbl == 2:
                if str(bSort.get()) == '1':
                    cur.execute("SELECT * FROM table2 ORDER BY Name")    #get all data from table by name
                elif str(bSort.get()) == '2':
                    cur.execute("SELECT *, CAST(SUBSTRING_INDEX(Exercise, '-', -1) AS UNSIGNED) as num FROM table2 ORDER BY num")      #get all data from table by exercise
                elif str(bSort.get()) == '3':
                    cur.execute("SELECT *, CAST(SUBSTRING_INDEX(Lesson, '-', -1) AS UNSIGNED) as num FROM table2 ORDER BY num")      #get all data from table by lesson
                else:
                    cur.execute("SELECT * FROM table2")

            #write to file--------------------------
            rows = cur.fetchall()           #get all records (in the table)
            f = open(self.openFile, "w")       #open text file
            for row in rows:
                print >>f, row["Name"], row["Lesson"], row["Exercise"], row["Appearance"]
            f.close()   #close text file
            #---------------------------------------
        
    def handleClose(self):
        print("Close")
    #symbols----------------------------------
    def handleAnd(self):
        print("And")
    def handleOr(self):
        print("Or")
    def handleNot(self):
        print("Not")
    def handleUndo(self):
    #edit--------------------------------------
        print("Undo")
    def handleRedo(self):
        print("Redo")
    #------------------------------------------

        
class Tables(Bottom):                                       #for purposes of creating tables
    def showTables(self, top, cur):
        tab = Tkinter.Button(top, text = "table1", command = lambda : self.handleTblSlct(top, cur, 1))
        tab.grid(row = 13, column = 18)
        tab = Tkinter.Button(top, text = "table2", command = lambda : self.handleTblSlct(top, cur, 2))
        tab.grid(row = 13, column = 19)
    def createTable(self, top, cur):
        #create a new table-----------------------------------
        #cur.execute("DROP TABLE IF EXISTS table1")
        #cur.execute("DROP TABLE IF EXISTS table2")
        cur.execute("CREATE TABLE IF NOT EXISTS table1(\
                    Name VARCHAR(100), Lesson VARCHAR(5), \
                    Exercise VARCHAR(5), Appearance VARCHAR(5))")
        cur.execute("CREATE TABLE IF NOT EXISTS table2(\
                    Name VARCHAR(100), Lesson VARCHAR(5), \
                    Exercise VARCHAR(5), Appearance VARCHAR(5))")
        #-----------------------------------------------------      if not exist

    def handleTblSlct(self, top, cur, table):
        global whichTbl
        whichTbl = table
        if whichTbl == 1:
            clear = Tkinter.Button(top, text = "clear table1", command = lambda : self.clearTable(top, cur, 1))                     #create button
            clear.grid(row = 12, column = 19)
        elif whichTbl == 2:
            clear = Tkinter.Button(top, text = "clear table2", command = lambda : self.clearTable(top, cur, 2))                     #create button
            clear.grid(row = 12, column = 19)
        self.printBottom(top, cur, 0, '', '', '', '')
    def clearTable(self, top, cur, table):
        yesNo = tkMessageBox.askokcancel("Clear", "You are about to clear selected table.")
        if yesNo:
            if whichTbl == 1:
                cur.execute("TRUNCATE TABLE table1")
            elif whichTbl == 2:
                cur.execute("TRUNCATE TABLE table2")
            self.printBottom(top, cur, 0, '', '', '', '')

        
    
def main():
    #mycolor = '#CCCC99'  # set rgb color for window
    top = Tkinter.Tk()
    top.title("WordTracker")
    #root.tk.call('wm', 'iconbitmap', self._w, '-default', '.ico') related to icon. Do at own pace, sweetie!
    #top.configure(bg = mycolor)
    lFrame = Left()

    try:
        db = MySQLdb.connect(               
            host = 'localhost',
            user = 'testuser',
            passwd = 'test623',
            db = 'testdb'
            )

        with db:                 #with is used by the interpreter to automatically release the resources, and to provide error
            cur = db.cursor(MySQLdb.cursors.DictCursor)  #traverse the records from the result set. Create curser of dictionary type
            
            lFrame.leftFrame(top, cur)

            top.mainloop()
    except MySQLdb.Error, e:
        print "Fin"

    finally:
        if db:
            db.close()
whichTbl = 1       #stores universal table name

main()




