# Creating a HDInsight cluster

Before you go on and create it, you would need to have these following things:
1) One Azure storage (Data lake storage gen 1) and make sure you create a folder in this so that you can provide this folder path when 
asked while creating the cluster (Root path)
2) One reource group
3) certificate related stuff, Azure AD service principal, this will represent the cluster when accessing Data Lake Storage Gen1 accounts.
(create new)
4) decide the cluster type (Spark)
