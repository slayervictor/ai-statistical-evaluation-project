#install.packages('rstudioapi')
library("rstudioapi")
HR <- read.csv(file.path(dirname(rstudioapi::getActiveDocumentContext()$path), "HR_data.csv"))
HR

hist(HR$HR_Max, breaks = 30) # breaks, er antal pillars, default er 10
hist(HR$HR_Min, breaks = 25)
hist(HR$HR_Mean, breaks = 25)
hist(HR$Frustrated, breaks = 6)

HR <- read.csv(file.path(dirname(rstudioapi::getActiveDocumentContext()$path), "HR_data_transformed.csv"))
HR
# 1. Make appropriate plots to investigate whether treatments or blocks have any influence on the fustration level

HR$HR_Mean <- as.factor(HR$HR_Mean)
HR$HR_Median <- as.factor(HR$HR_Median)
HR$HR_std <- as.factor(HR$HR_std)
HR$HR_Min <- as.factor(HR$HR_Min)
HR$HR_Max <- as.factor(HR$HR_Max)
HR$HR_AUC <- as.factor(HR$HR_AUC)
HR$Round <- as.factor(HR$Round)
HR$Phase <- as.factor(HR$Phase)
HR$Individual <- as.factor(HR$Individual)
HR$Puzzler <- as.factor(HR$Puzzler)
HR$Cohort <- as.factor(HR$Cohort)
boxplot(Frustrated ~ Puzzler, data = HR, main = "Frustration level per puzzler", ylab = "Frustration level")
boxplot(Frustrated ~ Cohort, data = HR, main = "Frustration level per cohort", ylab = "Frustration level")
boxplot(Frustrated ~ Individual, data = HR, main = "Frustration level per individual", ylab = "Frustration level")
boxplot(Frustrated ~ Phase, data = HR, main = "Frustration level per phase", ylab = "Frustration level")
boxplot(Frustrated ~ Round, data = HR, main = "Frustration level per round", ylab = "Frustration level")
boxplot(Frustrated ~ Phase + Round, data = HR, main = "Frustration level per round", ylab = "Frustration level")
boxplot(Frustrated ~ Phase + Individual, data = HR, main = "Frustration level per HR_Mean", ylab = "Frustration level")

L1 <- lm(Frustrated ~ Phase, data = HR)
anova(L1)
L2 <- lm(Frustrated ~ Round, data = HR)
anova(L2)
L3 <- lm(Frustrated ~ Phase * Round, data = HR)
anova(L3)
L4 <- lm(Frustrated ~ Individual, data = HR)
anova(L4)
L5 <- lm(Frustrated ~ Individual * Phase, data = HR)
anova(L5)
L6 <- lm(Frustrated ~ Individual * Round, data = HR)
anova(L6)
L7 <- lm(Frustrated ~ HR_Mean * Round, data = HR)
anova(L7)


# Is there an impact of being a puzzler on a) frustration level, b) heart rate?
L21 <- lm(Frustrated ~ Puzzler, data = HR)
anova(L21) #being a puzzler may not have a significant impact on frustration at the 0.05 significance level
L22 <- lm(Frustrated ~ HR_Mean, data = HR)
anova(L22) #being a puzzler may not have a statistically significant impact on the heart rate at the 0.05 significance level


