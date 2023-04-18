{ inputs, pkgs, ... }: let
  pkgs-stable = import inputs.nixpkgs-stable { system = pkgs.stdenv.system; };
in
{
  packages = [ pkgs.zlib ];

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    package = pkgs-stable.python311;
    poetry = {
      enable = true;
      package = pkgs-stable.poetry.override
        {
          python = pkgs-stable.python311;
        };
    };
  };
}
