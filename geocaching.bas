REM  *****  BASIC  *****

function lastRow(Sheets as object) as integer
	dim oCellCursor as object
	dim Sheet as object
	
	Sheet = ThisComponent.Sheets(0)
	oCellCursor = Sheets.createCursor
    oCellCursor.GotoEndOfUsedArea(False)
    nRow = oCellCursor.getRangeAddress().endRow
    lastRow = nRow
    
end function

sub writeNcorAndEcor()

Dim Doc As Object
Dim Sheet As Object   
dim iRun as integer
dim intLastRow as integer
dim strCell as string
dim strEcor as string
dim strNcor as string

iRun = 0
 
Doc = ThisComponent
Sheet = Doc.Sheets(0)

intLastRow = lastRow(Sheet)

    While iRun <> intLastRow + 1
    	strCell = CStr(Sheet.getCellByPosition(10,iRun).Value)
    	strNcor = "N " & Left(strCell,2) & "° " & Mid(strCell, 3, 2) & "." & Right(strCell,3)
		Sheet.getCellByPosition(12,iRun).setString(strNcor)
		
	 	strCell = CStr(Sheet.getCellByPosition(11,iRun).Value)
    	strEcor = "E 0" & Left(strCell,2) & "° " & Mid(strCell, 3, 2) & "." & Right(strCell,3)
		Sheet.getCellByPosition(13,iRun).setString(strEcor)
		
        iRun = iRun + 1
    Wend
    
End Sub

Sub Main
	call writeNcor
End Sub
