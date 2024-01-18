# How to Upload Your Graph to Lake FS
Theme 1 Teams, there are 3 ways to upload your graph to Lake FS. Instructions for two of those three ways is provided below. Instructions for the third method will soon follow.

Upload through the website

Upload using Amazon's Command Line Interface (CLI)

Upload using the Lake FS Command Line Interface (CLI)

For each method you will need to request credentials for accessing Lake FS. These credentials are an **Access Key ID** and a **Secret Access Key**. You may request these either by direct messaging Yaphet Kebede through our PROTO-OKN Slack Channel or by emailing Yahpet at kebedey at renci dot org. 



## Upload through the website

1. Navigate to [https://frink-lakefs.apps.renci.org/](https://frink-lakefs.apps.renci.org/auth/login?next=/repositories)

2. Enter your **Access Key ID** and your **Secret Access Key** to log in.

3. We request that you create one repository (repo) for each unique dataset (i.e., graph). Along with Lake FS's tagging system, this enables us to properly track versions of your graph. So when visiting Lake FS for the first time, please click the Create Repository button to create a new repo. 

4. The **Create A New Repository** pop-up window will appear asking you for a **Repository ID**. This is simply a name you wish to give your dataset/graph. The name must be in lowercase, may not contain spaces, and may contain dashes (-). You do not need to select any other settings in this pop-up. Once you have named your repo, click the **Create Repository** button.

5. Now that the repo has been created, click the **Upload Object** button to upload your dataset/graph.

6. The **Upload Object** pop-up window will appear offering you the option to drag and drop a single file from your desktop to the pop-up window. Once your file appears in the pop-up, click the **Upload** button to complete the upload. (Although there is a **Path** text field, it will not recognize a file path on your local machine. So please use the drag and drop feature.)

   Repeat this step for each file you need to upload.

7. Your upload is not complete until you commit the change to Lake FS. Click the **Uncommitted Changes** tab and you will see the upload you made in the previous steps. Click the **Commit Changes** button.

8. The **Commit Changes** pop-up window will appear. Please enter a **Commit Message** providing information about the nature of your upload. We suggest you include your name in case multiple individuals from your team are uploading files to Lake FS. The date and time will be recorded automatically. 

9. To mark the file(s) you uploaded in the above steps with a particular version number, you will need to create a **Tag**. Click on the **Tags** tab to do so.

   For more information on Lake FS tags, see https://docs.lakefs.io/understand/model.html

10. Once you are on the **Tags** tab, click the **Create Tag** button.

11. The **Create Tag** pop-up window will appear. Input a **Tag Name** in the field provided. It is sufficient to do this on the main branch. 

    Note: You may use other branches if you wish, just need to be sure to merge those branches back to main.

12. A tag in Lake FS works similarly to a Git ref name. A Lake FS tag marks all the files in the repo--i.e., the state of the repo--at the time the tag was created with that particular tag. So for example, on the **Objects** tab, there will be a drop-down menu with the different tags that have been added. Selecting one of those tags will show you all the files that were committed to the repo when that particular tag was created. Changing the selection in that drop-down also lets you access the different versions of your files. 

To upload a new version of a file(s) already uploaded to Lake FS, simply repeat steps 1 and 2, and 5 through 12. 

## Upload using Amazon's CLI



## Upload using the Lake FS CLI

