# How to Upload Your Graph to the Frink Landing Zone on Lake FS

Theme 1 Teams, there are 3 ways to upload your graph to Frink Landing Zone. Instructions for two of those three ways are provided below. Instructions for the third method (i.e., using the Lake FS CLI) will soon follow.

:key: **Access Keys** <br />
For each method you will need to have requested credentials for accessing the Frink Landing Zone. These credentials are an **Access Key ID** and a **Secret Access Key**. You may request these either by direct messaging Yaphet Kebede through the PROTO-OKN Slack Channel or by emailing Yahpet at kebedey at renci dot org. 

- [Upload through the website](#upload-through-the-website)

- [Upload using Amazon's Command Line Interface (CLI)](#amazon)

- [Upload using the Lake FS Command Line Interface (CLI)](#lakefs)


## Upload through the website

1. Navigate to [https://frink-lakefs.apps.renci.org/](https://frink-lakefs.apps.renci.org/auth/login?next=/repositories)

2. Enter your **Access Key ID** and your **Secret Access Key** to log in.

3. We request that you create one repository (repo) for each unique dataset (i.e., graph). Along with Lake FS's tagging system, this enables us to properly track versions of your graph. So when visiting Lake FS for the first time, please click the **Create Repository** button to create a new repo.

   <img width=20% alt="Create Repository button" src="https://github.com/frink-okn/frink-landing-zone/blob/main/img/1create-repo-button.png">

4. The **Create A New Repository** pop-up window will appear asking you for a **Repository ID**. This is simply a name you wish to give your dataset/graph. The name must be in lowercase, may not contain spaces, and may contain dashes (-). You do not need to select any other settings in this pop-up. Once you have named your repo, click the **Create Repository** button.

   <img width="60%" alt="Create A New Respository pop-up" src="https://github.com/frink-okn/frink-landing-zone/blob/main/img/2create-repo-popup.png">

5. Now that the repo has been created, click the **Upload Object** button to upload your dataset/graph.

   <img width="60%" alt="Upload Object button" src="https://github.com/frink-okn/frink-landing-zone/blob/main/img/3upload-object-button.png">

6. The **Upload Object** pop-up window will appear offering you the option to drag and drop a single file from your desktop to the pop-up window. Once your file appears in the pop-up, click the **Upload** button to complete the upload. (Although there is a **Path** text field, it will not recognize a file path on your local machine. So please use the drag and drop feature.)

    <img width=35% alt="Upload Object pop-up" src="https://github.com/frink-okn/frink-landing-zone/blob/main/img/4upload-object-popup.png">

    <br />

    :point_right: _**Repeat this step for each file you need to upload.**_

7. Your upload is not complete until you commit the change to Lake FS. Click the **Uncommitted Changes** tab and you will see the upload you made in the previous steps. Click the **Commit Changes** button.

    <img width="70%" alt="Uncommited Changes tab" src="https://github.com/frink-okn/frink-landing-zone/blob/main/img/5uncommitted-changes-tab.png">

8. The **Commit Changes** pop-up window will appear. Please enter a **Commit Message** providing information about the nature of your upload. We suggest you include your name in case multiple individuals from your team are uploading files to Lake FS. The date and time will be recorded automatically.

    <img width="40%" alt="Commit Changes pop-up" src="https://github.com/frink-okn/frink-landing-zone/blob/main/img/7commit-changes-popup.png">

9. To mark the file(s) you uploaded in the above steps with a particular version number, you will need to create a **Tag**. Click on the **Tags** tab to do so.
   
    <img width="70%" alt="Tags tab" src="https://github.com/frink-okn/frink-landing-zone/blob/main/img/9tags-tab-button.png">

10. Once you are on the **Tags** tab, click the **Create Tag** button. For more information on Lake FS tags, see https://docs.lakefs.io/understand/model.html

11. The **Create Tag** pop-up window will appear. Input a **Tag Name** in the field provided. It is sufficient to do this on the main branch.

    <img width="40%" alt="Create Tag pop-up" src="https://github.com/frink-okn/frink-landing-zone/blob/main/img/10tag-popup.png">
    
    :point_right: _**You may use other branches if you wish, just be sure to merge those branches back to main.**_

12. A tag in Lake FS works similarly to a Git ref name. A Lake FS tag marks all the files in the repo--i.e., the state of the repo--at the time the tag was created with that particular tag. So for example, on the **Objects** tab, there will be a drop-down menu with the different tags that have been added. Selecting one of those tags will show you all the files that were committed to the repo when that particular tag was created. Changing the selection in that drop-down also lets you access the different versions of your files.

    <img width="40%" alt="Committed changes by tag" src="https://github.com/frink-okn/frink-landing-zone/blob/main/img/11change-committed-per-tag.png">

To upload a new version of a file(s) already uploaded to the Frink Landing Zone, simply repeat all steps except 


## Upload using Amazon's CLI

YAPHET


## Upload using the Lake FS CLI

This information will be available soon.
