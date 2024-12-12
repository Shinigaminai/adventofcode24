program day12;

{$mode objfpc}

uses
  Classes,SysUtils;

const
  C_FNAME = 'day12.test.txt';

type
  size2d = record
      width: integer;
      height: integer;
  end;

type
  Grid = array of string;
var
  slInfo: TStringList;
  input_grid: Grid;
  input_size: size2d;
  fin: TextFile;
  line: string;
  i: Integer;
begin
  slInfo := TStringList.Create;
  try
    // Open the file for reading
    slInfo.LoadFromFile(C_FNAME);
    writeln(slInfo.Count);
    i := 0;
    while i < slInfo.Count do
    begin
      writeln(slInfo[i]);
      inc(i);
    end;
  except
    // If there was an error the reason can be found here
    on E: EInOutError do
      writeln('File handling error occurred. Reason: ', E.Message);
  end;
  slInfo.Free;
end.
