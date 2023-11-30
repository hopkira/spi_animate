import shutil
source_prefix = "/home/hopkira/spi_animate/images/"
target_prefix = "/var/tmp/"
for x in range(90):
    source = source_prefix + "frame_{0:02d}_delay-0.06s.gif".format(x)
    target = target_prefix + "01_{0:02d}.gif".format(x)
    shutil.copyfile(source, target)
    print(source,"->",target)