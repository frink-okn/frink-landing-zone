# How to Upload Your Graph to the FRINK Landing Zone
Theme 1 Teams, there are several ways to upload your graph to the FRINK Landing Zone found on lakeFS. We recommend uploading through the website for smaller files and using Amazon's S3 Tool for larger files or for automating the process. 

!!! note

    For each method, you will need to request credentials for accessing lakeFS. These credentials are an **Access Key ID** and a **Secret Acess 
    Key**. You may request these either by direct messaging Yaphet Kebede through our PROTO-OKN Slack channel or by emailing Yaphet at kebedey at
    renci dot org.

??? warning
   
    We are currently trying to resolve a problem with extremely large files (e.g., 100GB or more). If you run into a problem uploading your file and 
    it is around or over 100GB, please contact Yaphet Kebede at kebedey at renci dot org.

## Upload through the website

1. Navigate to [https://frink-lakefs.apps.renci.org/](https://frink-lakefs.apps.renci.org/)

2. Enter your **Access Key ID** and your **Secret Access Key** to log in.

3. We request that you create one repository (repo) for each unique dataset (i.e., graph). Along with lakeFS' tagging system, this enables us to properly track versions of your graph. So when visiting lakeFS for the first time, please click the **Create Repository** button to create a new repo.    
<img src="../../assets/images/1create-repo-button.png" width="200">

4. The **Create A New Repository** pop-up window will appear asking you for a **Repository ID**. This is simply a name you wish to give your dataset/graph. The name must be in lowercase, may not contain spaces, but may contain dashes (-). You do not need to select any other settings in this pop-up. Once you have named your repo, click the **Create Repository** button.   
<img src="../../assets/images/2create-repo-popup.png">

5. Now that the repo has been created, click the **Upload Object** button to upload your dataset/graph.   
<img src="../../assets/images/3upload-object-button.png">

6. The **Upload Object** pop-up window will appear offering you the option to drag and drop a single file from your desktop to the pop-up window. Once your file appears in the pop-up, click the **Upload** button to complete the upload. (Although there is a **Path** text field, it will not recognize a file path on your local machine. So please use the drag and drop feature.)
<img src="../../assets/images/4upload-object-popup.png" width="400">     

	!!! warning ""

	 	**Repeat this step for each file you need to upload.** 
	 
7. Your upload is not complete until you commit the change to lakeFS. Click the **Uncommitted Changes** tab and you will see the upload you made in the previous steps. Click the **Commit Changes** button.<img src="../../assets/images/5uncommitted-changes-tab.png">
8. The **Commit Changes** pop-up window will appear. Please enter a **Commit Message** providing information about the nature of your upload. We suggest you include your name in case multiple individuals from your team are uploading files to lakeFS. The date and time will be recorded automatically.  
<img src="../../assets/images/7commit-changes-popup.png" width="400">

9. To mark the file(s) you uploaded in the above steps with a particular version number, you will need to create a **Tag**. Click on the **Tags** tab to do so.   
<img src="../../assets/images/9tags-tab-button.png">
10. Once you are on the **Tags** tab, click the **Create Tag** button.  

	!!! info

	 	For more information on Lake FS tags, see [https://docs.lakefs.io/understand/model.html#tags](https://docs.lakefs.io/understand/model.html#tags)
	 
11. The **Create Tag** pop-up window will appear. Input a **Tag Name** in the field provided. It is sufficient to do this on the main branch.  
<img src="../../assets/images/10tag-popup.png" width="400"> 

	!!! info ""

	 	You may use other branches if you wish, just be sure to merge those branches back to main. 
	 

12. A tag in lakeFS works similarly to a Git ref name. A lakeFS tag marks all the files in the repo&mdash;i.e., the state of the repo&mdash;at the time the tag was created with that particular tag. So for example, on the **Objects** tab, there will be a drop-down menu with the different tags that have been added. Selecting one of those tags will show you all the files that were committed to the repo when that particular tag was created. Changing the selection in that drop-down also lets you access the different versions of your files.
<img src="../../assets/images/11change-committed-per-tag.png">

!!! info ""

	 **To upload a new version of a file(s) already uploaded to lakeFS, simply repeat steps 1 and 2, and 5 through 12.**


!!! info

     See the <a href="https://docs.lakefs.io/quickstart/">lakeFS QuickStart guide</a> for more information.</strong></font> 
  
  
## Upload Using Amazon's S3 Command Line Interface (CLI) Tool

!!! info

     More details about using the AWS CLI can be found at <a href="https://docs.lakefs.io/integrations/aws_cli.html">Using lakeFS with the AWS CLI</a>.     
    
     
1. Install the AWS CLI Toolkit.
    * Follow the steps in the [AWS CLI installation guide](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html) to install the AWS CLI toolkit.
    
2. Set up an AWS profile. Creating a profile makes it easier to switch between different AWS services and lakeFS.
    * Open a new terminal.
    * Configure a profile for lakeFS using your **Access Key ID** and **Secret Access Key**:
    ```
    aws configure --profile lakefs
    ```
    
3. Create a lakeFS repository.
    * Visit the [Frink Landing Zone on lakeFS](https://frink-lakefs.apps.renci.org) in a web browser.
    * Click the **Create Repository** button to create a new repo.  
    <img src="../../assets/images/1create-repo-button.png" width="200"">
    * The **Create A New Repository** pop-up window will appear asking you for a **Repository ID**. This is simply a name you wish to give your dataset/graph. The name must be in lowercase, may not contain spaces, but may contain dashes (-). You do not need to select any other settings in this pop-up. Once you have named your repo, click the **Create Repository** button.
    <img src="../../assets/images/2create-repo-popup.png">
    
4. Upload files to the repository.
    * In the terminal, upload files to the new repository on the main branch:
    ``` 
    aws s3 cp my-local-dataset.hdt s3://my-repo/main/my-local-graph.hdt --endpoint="https://frink-lakefs.apps.renci.org" --profile lakefs
	```

    * This example will copy `my-local-dataset.hdt` file to a repo called `my-repo` on the `main` branch, renamed as `my-local-graph.hdt`. It forces the s3 tool to target FRINK lakefs by providing the `--endpoint` option.
5. Commit the upload.
    * Back in the web browser, go to your repository.
    * Navigate to the **Uncommitted Changes** tab. Click the **Commit Changes** button.   
     <img src="../../assets/images/5uncommitted-changes-tab.png">  
    * The **Commit Changes** pop-up window will appear. Please enter an appropriate **Commit Message**.  
     <img src="../../assets/images/7commit-changes-popup.png" width="400">
     
6. Mark as a release and create tags. If you need to mark this as a release and create tags, follow steps 9 onward in the **Upload through the website** section above. 

!!! info

    This could work with other s3 clients. Possible options are also listed at <a href="https://docs.lakefs.io/howto/copying.html">Copying Data
    to/from lakeFS</a>.

