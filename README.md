My goal is to see if I can host two python packages in the same repository, and 
include some source files in both packages via symlinks.  The specific 
motivation is my `macromol_training` repository, which I want to break into two 
packages: one for building the database and another for training with it.  
However, both of these packages would need access to the general-purpose 
database IO functions.
