{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  nativeBuildInputs = [ pkgs.hugo (pkgs.python3.withPackages  (ps: [ps.requests])) pkgs.proselint ];
}
