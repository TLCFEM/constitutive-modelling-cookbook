# Constitutive Modelling Cookbook

\[Work In Progress\] A reference book on constitutive modelling.

The following models are covered.

 * Uniaxial Metal Models
    * Linear Isotropic Hardening Model
    * Combined Isotropic/Kinematic Hardening Model
    * Armstrong-Fredrick Hardening Model
    * Armstrong-Fredrick with Strain Memory
    * Subloading Surface Model
    * Uniaxial Model for BRB Steel
    * VAFCRP1D
 * Uniaxial Phenomenological Models
    * Ramberg-Osgood Model
    * MPF Steel Model
    * Bouc-Wen Model
    * BWBN Model
    * General Framework for Hysteresis Models
 * Uniaxial Plasticity Models (Other Materials)
    * K4 Concrete
 * Viscoplasticity
    * VAFCRP Model
    * Maxwell Model
 * Metal
    * von Mises Framework
    * Extended Subloading Surface Model
    * Orthotropic Hoffman Model
    * YLD0418P
 * Timber
    * TimberPD
 * Concrete
    * Concrete Damage Plasticity (CDP) Model
    * CDPM2 Model
 * Rubber
    * Basic Quantities
    * Mooney-Rivlin Model
    * Blatz-Ko Model
    * Yeoh Model
 * Geomaterial
    * Drucker-Prager Model
    * Modified Cam Clay Model
    * Simple Sand Model
    * Dafalias-Manzari Sand Model
    * Duncan Soil Model
 * Other
    * Gurson's Void Growth Model
    * The $N$-$M$ Frame Element


## To Build

The following commands can be used to compile this book with docker.
Please make sure `docker` and `curl` are available on the system.

```bash
mkdir -p cookbook
curl -fsSL https://raw.githubusercontent.com/TLCFEM/constitutive-modelling-cookbook/master/dockerfile -o cookbook/dockerfile

docker build -f cookbook/dockerfile -t cookbook cookbook

cid=$(docker create cookbook)
docker cp "$cid:/workspace/COOKBOOK.pdf" .
docker rm "$cid" >/dev/null
```