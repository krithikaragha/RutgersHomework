Sub Easy()

Dim totalVolume As Double
Dim j, rowcount As Integer

j = 1
totalVolume = 0

' Count the number of rows
rowcount = Cells(Rows.Count, 1).End(xlUp).Row

For i = 2 To rowcount:

   totalVolume = totalVolume + Cells(i, 7).Value

   ' If ticker changes, then print results
   If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

       ' Update j value
       j = j + 1

       ' Stores results in variable
       totalVolume = totalVolume + Cells(i, 7).Value

       ' Print the ticker symbol
       Range("I" & j).Value = Cells(i, 1).Value

       ' Print total volume
       Range("J" & j).Value = totalVolume

       ' Reset total volume
       totalVolume = 0

   End If

Next i

End Sub
