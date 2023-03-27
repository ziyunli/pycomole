{ pkgs, ... }:

{
  packages = [ pkgs.zlib ];

  # https://devenv.sh/languages/
  # languages.nix.enable = true;
    languages.python = {
    enable = true;
    poetry.enable = true;
  };

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # https://devenv.sh/processes/
  # processes.ping.exec = "ping example.com";

  # See full reference at https://devenv.sh/reference/options/
}
