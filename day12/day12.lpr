{$mode objfpc}

program day12;

uses
  Classes,SysUtils,Position;

const
  C_FNAME = 'day12.input.txt';

type
  StrLptr = ^TStringList;
  TRegion = record
    area, circ: Integer;
  end;
    

function isValidIndex(pos: TPosition; maxPosition: TPosition): Boolean;
begin
  if (pos.y < 0) or (pos.y > maxPosition.y) or (pos.x < 1) or (pos.x > maxPosition.x) then
    Exit(False);
  Result := True;
end;

function calculateRegion(pos: TPosition; map: StrLptr): TRegion;
var
  directions: array of TPosition;
  recRegion: TRegion;
  nextPosition: TPosition;
  plot, plotVisited: Char;
  dir: TPosition;
  nextPlot: Char;
  plotptr: ^Char;
begin
  Result.area := 1;
  Result.circ := 0;
  plot := map^[pos.y][pos.x];
  plotVisited := Chr(Ord(plot) + 32);
  plotptr := @map^[pos.y][pos.x];
  plotptr^ := plotVisited;
  directions := [TPosition.Create(0,1), TPosition.Create(0, -1), TPosition.Create(-1, 0), TPosition.Create(1, 0)];
  for dir in directions do
  begin
    nextPosition := TPosition.Create(pos.x + dir.x, pos.y + dir.y);
    // writeln('nextpos ', nextPosition.y, ',', nextPosition.x);
    if not isValidIndex(nextPosition, TPosition.Create(Length(map^[0]), map^.Count - 1)) then
    begin
      inc(Result.circ);
      Continue;
    end;
    nextPlot := map^[nextPosition.y][nextPosition.x];
    if nextPlot = plot then
    begin
      recRegion := calculateRegion(nextPosition, map);
      Result.area += recRegion.area;
      Result.circ += recRegion.circ;
      Continue;
    end;
    if nextPlot = plotVisited then
      Continue;
    inc(Result.circ);
  end;
end;

function calcFencing(map: StrLptr): Integer;
var
  i, j: Integer;
  line: String;
  recRegion: TRegion;
  plot: char;
  plotptr: string;
  mapVal: TStringList;
begin
  Result := 0;
  i := 0;
  writeln('iterate ', map^.Count, ' lines');
  while i < map^.Count do
  begin
    j := 1;
    line := map^[i];
    // writeln(line);
    while j <= (Length(line)) do
    begin
      if (map^[i][j] <= 'Z') and (map^[i][j] >= 'A') then
      begin
        plot := map^[i][j];
        // writeln('checking plot ', i, ',', j, ': ', plot);
        recRegion := calculateRegion(TPosition.Create(j, i), map);
        Result += recRegion.area * recRegion.circ;
        writeln('Found new Region ', plot, ' of area ', recRegion.area, ' and circ ', recRegion.circ);
      end;
      inc(j);
    end;
    inc(i);
  end;
end;

var
  slInfo: TStringList;
  i: Integer;
begin
  slInfo := TStringList.Create;
  try
    // Open the file for reading
    slInfo.LoadFromFile(C_FNAME);
    writeln(slInfo.Count);
    // Lines start at index 0, Columns at index 1 !! :(
    // i := 0;
    // while i < slInfo.Count do
    // begin
    //   writeln(slInfo[i]);
    //   inc(i);
    // end;
    writeln(calcFencing(@slInfo))
  except
    // If there was an error the reason can be found here
    on E: EInOutError do
      writeln('File handling error occurred. Reason: ', E.Message);
  end;
  slInfo.Free;
end.
