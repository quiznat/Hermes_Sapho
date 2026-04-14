---
version: source-capture.v1
article_id: art-2026-04-14-001
ticket_id: ticket-import-art-2026-04-14-001
source_url: https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-github-pages/
canonical_url: https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-github-pages
source_title: 'GitHub for Beginners: Getting started with GitHub Pages - The GitHub
  Blog'
capture_kind: html
http_status: 200
content_type: text/html
captured_at_utc: '2026-04-14T13:01:15Z'
linked_paper_urls: []
---
# Source Capture

## Title

GitHub for Beginners: Getting started with GitHub Pages - The GitHub Blog

## Body

Home / Developer skills / GitHub

GitHub for Beginners: Getting started with GitHub Pages

Learn how to create a free website for any repository on GitHub Pages.

Kedasha Kerr · @ladykerr

April 13, 2026
| 4 minutes

Share:

Welcome back to GitHub for Beginners. So far, we’ve discussed GitHub Issues and Projects , GitHub Actions , and covered a bit about security . This time, we’re going to talk about GitHub Pages.

Did you know that you have access to a free and secure hosting service on GitHub, readily available for any project? That’s what GitHub Pages is—a way to turn any GitHub repository with a static website into a live site for free. You just need three things:

A GitHub account

A project to deploy

A few minutes to deploy to GitHub Pages

Follow the steps in this blog and your project will be live, searchable, and ready to share. Let’s get started!

As always, if you prefer to watch the video or want to reference it, we have all of our GitHub for Beginners episodes available on YouTube .

Deploying to GitHub Pages

To get started, navigate to the sample repository , and create a fork of the repository that you can use for your own walkthrough. This repository has a static website generated with Next.js. Since it’s already been pushed up to GitHub, it’s ready to deploy.

There are two different ways that you can deploy your project to GitHub Pages: deploying from a branch or using GitHub Actions. First, let’s look at deploying from a branch.

Select the Settings tab at the top of the repository.

Select Pages from the left-hand menu. It’s located in the “Code and automation” section of the settings.

Use the combo box under “Build and deployment” and select Deploy from a branch .

Under “Branch,” use the combo box to select main as the branch to deploy from.

Click Save .

This publishes the website from the main branch and makes it publicly available.

Deploying with GitHub Actions

Now let’s look at publishing using the GitHub Actions workflow. Since we’re already on the appropriate Settings page, we’ll pick up from here.

Under “Source,” use the combo box and select GitHub Actions . Once you do, GitHub will provide some suggested workflows.

Select browse all workflows to see all the possible workflows available.This will send you to a new page with all sorts of workflows for different languages.

Enter “next.js” into the search box to filter the possible workflows.

Click the Configure button in the “Next.js” workflow box. This takes you to the workflow file.

Review the file and verify the permissions that are set as well as the build and deploy instructions.

Since the file does not require any changes, select the green Commit changes button at the top-right of the window.

Provide a commit message or have Copilot create one for you.

Make sure the option to commit to the main branch is selected, then click Commit changes at the bottom of the window.

Once the changes have been committed, select the Actions tab and wait for the actions to complete.

Select the name of the Add GitHub Actions workflow for Next.js deployment action. Note that there will be two actions with the same name. If the action has successfully completed and does not show a website link in the “deploy” box, you want to go back and select the other action with an identical name.

Select the link in the “deploy” box to see your website hosted on GitHub Pages.

Congratulations! You have successfully deployed a website to GitHub Pages. Keep in mind that even if your repository is private, the published website will still be public. If you ever want to see who most recently deployed your website, you can do so by navigating back to Settings -> Pages .

Adding a custom domain

By default, all websites on GitHub Pages will have the following URL: USERNAME.github.io/REPOSITORY-NAME .

However, you can update this to use your custom domain if you want. To do this, you’ll first need to configure DNS records with your domain provider. You can read more about how to do this by checking out our docs on managing a custom domain . You’ll also need to verify your domain at the org or profile level.

Once you’ve configured the DNS records and verified the domain, you can set the custom domain by following these steps:

Navigate to Settings -> Pages .

Under “Custom domain,” enter your domain name into the box provided.

Select Save next to your custom domain. After you update the domain name, GitHub automatically checks your domain’s DNS configuration. If everything seems good, you’ll see a green checkmark.

Once the domain has been verified, select the Enforce HTTPS checkbox. This secures your site with a free SSL certificate and makes sure visitors see that secure padlock in their browser.

What’s next?

Now you know how to select a project to deploy and create a website for the repository either from a branch or by using GitHub Actions. Not only that, but you can customize the domain, and it’s all available for free! Use this to promote your projects, share what you’re working on, or expand your portfolio, even if the projects themselves are private.

If you want to learn more about GitHub Pages, here are some good places to get started:

The GitHub Pages main doc site

Creating a GitHub Pages site

About custom domains

Happy coding!

Tags:

GitHub for beginners

GitHub Skills

Written by

Kedasha Kerr

@ladykerr

Kedasha is a Developer Advocate at GitHub where she enjoys sharing the lessons she's learned with the wider developer community. She finds joy in helping others learn about the tech industry and loves sharing her experience as a software developer. Find her online @itsthatladydev.
