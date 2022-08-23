
from battery_diffusion.solver.mesher import Mesh
from battery_diffusion.solver.fem_wrapper import FEM
from skimage.data import binary_blobs
from nanomesh import Image
#setup for the mesh
length=100
blobs=binary_blobs(length=length, volume_fraction=0.20,seed=2102)
plane=Image(blobs)
Diffusivity_coefficient={"lithium":0.00005 ,"electrolyte":0.05}

# This is weird, you create two instance of the same object with the same parameter !
mesh=Mesh(plane=plane,length=length).skfem_mesher()
basis=Mesh(plane=plane,length=length).basis_laplace()
basis2=Mesh(plane=plane,length=length).basis_electrolyte()


initial=FEM(dt=0.01,t_max=500,initial_temp=200,mesh=mesh,basis=basis,basis2=basis2,Diffusivity_coefficient=Diffusivity_coefficient)
initial.simulate()
