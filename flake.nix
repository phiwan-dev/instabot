{
    description = "Python 3.12 development environment";

    #inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-24.11";
    inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

    outputs = { self, nixpkgs }:
    let
        system = "x86_64-linux";
        pkgs = import nixpkgs { inherit system; config.cudaSupport = true; config.allowUnfree = true; };
    in {
        devShells.${system}.default = pkgs.mkShell {
            buildInputs = with pkgs; [

                python312
                (with python312Packages; [
                    requests

                    # flux
                    huggingface-hub
                    pillow
                    torch
                    diffusers
                    bitsandbytes
                    transformers sentencepiece
                    accelerate
                    sympy
                    optimum

                    # llm
                    langchain-ollama
                ])
            ];
        };
    };
}

