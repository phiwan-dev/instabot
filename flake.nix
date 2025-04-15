{
    description = "Cuda development environment. Can be used with the python uv package manager to imperatively install packages like pytorch.";

    #inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-24.11";       Uses the cuda driver installed on the system, hence commented out.
    #inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";    Forcing a specific version will likely result in conflicts!

    outputs = { self, nixpkgs }:
    let
        system = "x86_64-linux";
        pkgs = import nixpkgs { inherit system; config.cudaSupport = true; config.allowUnfree = true; };
    in {
        devShells.${system}.default = pkgs.mkShell {

            buildInputs = with pkgs; [
                cudaPackages.cuda_cudart
                cudaPackages.cuda_nvcc
                cudaPackages.cuda_cccl
                linuxPackages.nvidia_x11
            ];

            shellHook = ''
                # NVIDIA Driver and CUDA setup
                export NVIDIA_VISIBLE_DEVICES=all
                export NVIDIA_DRIVER_CAPABILITIES=compute,utility
                export CUDA_VISIBLE_DEVICES=0

                # Path setup
                export PATH="${pkgs.gcc12}/bin:$PATH"
                export PATH=${pkgs.cudaPackages.cuda_nvcc}/bin:$PATH

                # CUDA setup
                export CUDAHOSTCXX="${pkgs.gcc12}/bin/g++"
                export CUDA_HOST_COMPILER="${pkgs.gcc12}/bin/gcc"
                export CUDA_HOME=${pkgs.cudaPackages.cuda_cudart}
                export CUDA_PATH=${pkgs.cudaPackages.cuda_cudart}

                # Library paths with specific NVIDIA driver
                export LD_LIBRARY_PATH=${pkgs.linuxPackages.nvidia_x11}/lib
                export LD_LIBRARY_PATH=${pkgs.cudaPackages.cuda_cudart}/lib64:${pkgs.cudaPackages.cuda_cudart}/lib:$LD_LIBRARY_PATH
                export LD_LIBRARY_PATH={pkgs.stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH

                export LIBRARY_PATH=${pkgs.cudaPackages.cuda_cudart}/lib64:${pkgs.cudaPackages.cuda_cudart}/lib:$LIBRARY_PATH

                # OpenGL driver path
                export LD_LIBRARY_PATH=${pkgs.linuxPackages.nvidia_x11}/lib:$LD_LIBRARY_PATH

                nvcc --version
            '';
        };
    };
}

