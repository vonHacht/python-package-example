import pip, site

installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])

print("Packages: \n" + str(installed_packages_list) + "\n")
print("Destinations: \n" + str(site.getsitepackages()))
