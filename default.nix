{ pkgs ? import <nixpkgs> {} }:
pkgs.stdenv.mkDerivation {
  pname = "me-michciooo";
  version = "0.1.0";
  src = ./.;
  buildInputs = [ pkgs.hugo ];
  dontBuild = true;
  installPhase = ''
    hugo --destination $out/share/meekchoppes
  '';
}
