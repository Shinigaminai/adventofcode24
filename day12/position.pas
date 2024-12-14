{$mode objfpc}{$H+}{$M+}

unit position;

interface

type
  TPosition = class
    public
      x, y: Integer;
      Constructor Create(cx, cy: Integer);
  end;

implementation

constructor TPosition.Create(cx, cy: Integer);
begin
  x := cx;
  y := cy;
end;
end.