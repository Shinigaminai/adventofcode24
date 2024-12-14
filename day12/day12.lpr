{$mode objfpc}

program day12;

uses
  Classes,SysUtils,Position;

const
  C_FNAME = 'day12.test.txt';

type
  StrLptr = ^TStringList;
  TRegion = record
    area, circ: Integer;
  end;
    

function isEqualNeighbor(pos: TPosition; dir: TPosition; map: TStringList): Integer;
var
  maxPosition: TPosition;
  nextPosition: TPosition;
begin
  maxPosition := TPosition.Create((Length(map[0]) - 1), map.Count - 1);
  nextPosition := TPosition.Create(pos.x + dir.x, pos.y + dir.y);
  if (nextPosition.y < 0) or (nextPosition.y > maxPosition.y) or (nextPosition.x < 0) or (nextPosition.x > maxPosition.x) then
    Exit(0);
  if map[nextPosition.y][nextPosition.x] = map[pos.y][pos.x] then
    Exit(1);
  Result := 0;
end;

function calculateRegion(pos: TPosition; map: StrLptr): TRegion;
var
  directions: array of TPosition;
  recRegion: TRegion;
  nextPosition: TPosition;
  plot, plotVisited: Char;
  dir: TPosition;
begin
  Result.area := 1;
  Result.circ := 0;
  plot := map^[pos.y][pos.x];
  plotVisited := Chr(Ord(plot) + 20);
  map^[pos.y][pos.x] := plotVisited;
  directions := [TPosition.Create(0,1), TPosition.Create(0, -1), TPosition.Create(-1, 0), TPosition.Create(1, 0)];
  for dir in directions do
  begin
    nextPosition := TPosition.Create(pos.x + dir.x, pos.y + dir.y);
    case map^[nextPosition.y][nextPosition.x] of
      plot:
        begin
          recRegion := calculateRegion(nextPosition, map);
          Result.area += recRegion.area;
          Result.circ += recRegion.circ;
        end;
      plotVisited:
        Continue
    else
      Result.circ += 1;
    end;
  end;
end;

function calcFencing(map: StrLptr): Integer;
var
  i, j: Integer;
  line: String;
  directions: array of TPosition;
  dir: TPosition;
  recRegion: TRegion;
  plot: char;
begin
  Result := 0;
  i := 0;
  directions := [TPosition.Create(0,1), TPosition.Create(0, -1), TPosition.Create(-1, 0), TPosition.Create(1, 0)];
  while i < map^.Count do
  begin
    j := 0;
    line := map^[i];
    while j < (Length(line) - 1) do
    begin
      if map^[i][j] < 'a' then
      begin
        plot := map^[i][j];
        recRegion := calculateRegion(TPosition.Create(j, i), map);
        Result += recRegion.area * recRegion.circ;
        writeln('Found new Region ', plot, ' of area ', recRegion.area, ' and circ ', recRegion.circ);
      end;
      j := j + 1;
    end;
    i := i + 1;
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
