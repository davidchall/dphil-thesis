void mT_ww_df() 
{
   // Axis ranges
   Float_t minX = 61.;
   Float_t maxX = 199.;
   Float_t minY = 0.83;
   Float_t maxY = 1.28;
   Color_t colPSUE  = kBlue;
   Color_t colNLOPS = kGreen;
   Color_t colScale = kRed;


   //------------------
   //   Setup pads
   //------------------
   TCanvas *c1 = new TCanvas("c1", "canvas", 600, 800);
   // Number of pads
   const Int_t Nx = 2;
   const Int_t Ny = 3;
   // Margins
   Float_t lMargin = 0.12;
   Float_t rMargin = 0.05;
   Float_t bMargin = 0.15;
   Float_t tMargin = 0.05;
   // Canvas setup
   CanvasPartition(c1,Nx,Ny,lMargin,rMargin,bMargin,tMargin);

   // Retrieve pads
   TPad *pad[Nx][Ny];
   TH1F *frame[Nx][Ny];
   for (Int_t i=0;i<Nx;i++) {
      for (Int_t j=0;j<Ny;j++) {
         c1->cd(0);
         char pname[16];
         sprintf(pname,"pad_%i_%i",i,j);
         pad[i][j] = (TPad*) gROOT->FindObject(pname);

         // Draw the pad's frame
         pad[i][j]->cd();
         frame[i][j] = pad[i][j]->DrawFrame(minX, minY, maxX, maxY);
         frame[i][j]->SetLabelFont(43, "xy");
         frame[i][j]->SetLabelSize(18, "xy");
         frame[i][j]->SetTitleFont(43, "xy");
         frame[i][j]->SetTitleSize(18, "xy");
         frame[i][j]->SetTitleOffset(2.6, "x");
         frame[i][j]->SetTickLength(0.0, "xy");
         c1->cd();
      }
   }
   // Bottom pads only
   for (Int_t i=0;i<Nx;i++) {
      frame[i][0]->GetXaxis()->SetTickLength(0.03);
      frame[i][0]->GetXaxis()->SetNdivisions(10, 2, 0, kTRUE);
      frame[i][0]->GetXaxis()->SetTitle("#it{m}_{T} [GeV]");
   }
   // Left pads only
   for (Int_t j=0;j<Ny;j++) {
      frame[0][j]->GetYaxis()->SetTickLength(0.03);
      frame[0][j]->GetYaxis()->SetNdivisions(5, 2, 0, kTRUE);
   }



   TFile *file = new TFile("ww.root", "read");
   TGraphErrors *h_psue[Nx][Ny], *h_model[Nx][Ny], *h_scale[Nx][Ny];
   TF1 *fit[Nx][Ny], *fitinv[Nx][Ny];

   // Horizontal lines
   TLine *centre_line = new TLine(minX, 1.0, maxX, 1.0);
   centre_line->SetLineStyle(1);
   TLine *hi_line = new TLine(minX, 1.1, maxX, 1.1);
   hi_line->SetLineStyle(3);
   TLine *lo_line = new TLine(minX, 0.9, maxX, 0.9);
   lo_line->SetLineStyle(3);

   TString colName[2]  = {"sr1", "sr2"};
   TString colLabel[2] = {"#it{m}_{ll} < 30 GeV", "#it{m}_{ll} > 30 GeV"};
   TString rowName[3]  = {"slep20", "slep15", "slep10"}; // count from bottom row
   TString rowLabel[3] = {"#it{p}_{T,l}^{sublead} > 20 GeV", "#it{p}_{T,l}^{sublead}#in[15,20] GeV", "#it{p}_{T,l}^{sublead}#in[10,15] GeV"};
   TString commonName  = "df_0j";
   TLatex *label[Nx][Ny];


   for (Int_t i=0;i<Nx;i++) {
      for (Int_t j=0;j<Ny;j++) {
         pad[i][j]->cd();

         // PS/UE
         h_psue[i][j] = ConvertHistToBand((TH1D*)file->Get(rowName[j]+"_"+colName[i]+"_"+commonName+"_PSUE"), minX, maxX);
         h_psue[i][j]->SetFillColor(colPSUE);
         h_psue[i][j]->SetFillStyle(3001);
         h_psue[i][j]->Draw("3 same");

         // NLO-PS
         h_model[i][j] = ConvertHistToBand((TH1D*)file->Get(rowName[j]+"_"+colName[i]+"_"+commonName+"_Model"), minX, maxX);
         h_model[i][j]->SetFillColor(colNLOPS);
         h_model[i][j]->SetFillStyle(3354);
         h_model[i][j]->Draw("3 same");

         // Scale
         h_scale[i][j] = ConvertHistToBand((TH1D*)file->Get(rowName[j]+"_"+colName[i]+"_"+commonName+"_Scale"), minX, maxX);
         h_scale[i][j]->SetFillColor(colScale);
         h_scale[i][j]->SetFillStyle(3345);
         h_scale[i][j]->Draw("3 same");

         // Fit
         TString fitname = "f_"+rowName[j]+"_"+colName[i]+"_"+commonName;
         fit[i][j] = (TF1*)file->Get(fitname);
         // adjust flat sections of DF 0j SR2c
         if (colName[i] == "sr2" && rowName[j] == "slep20" && commonName == "df_0j") {
            TString fitfunction = fit[i][j]->GetTitle();
            fitfunction.ReplaceAll("x<65", "x<90");
            fitfunction.ReplaceAll("x>=65", "x>=90");
            fitfunction.ReplaceAll("x>180", "x>170");
            fitfunction.ReplaceAll("x<=180", "x<=170");
            fitfunction.ReplaceAll("0.912243", "0.947958");
            fitfunction.ReplaceAll("1.076435", "1.062198");
            fit[i][j] = new TF1(fitname, fitfunction, minX, maxX);
            fit[i][j]->SetLineColor(fit[0][0]->GetLineColor());
            fit[i][j]->SetLineWidth(fit[0][0]->GetLineWidth());
            fit[i][j]->SetLineStyle(fit[0][0]->GetLineStyle());
         }
         fit[i][j]->Draw("same");
         fitinv[i][j] = new TF1(fitname+"_inv", "1.0/"+fitname, minX, maxX);
         fitinv[i][j]->SetLineColor(fit[i][j]->GetLineColor());
         fitinv[i][j]->SetLineWidth(fit[i][j]->GetLineWidth());
         fitinv[i][j]->SetLineStyle(fit[i][j]->GetLineStyle());
         fitinv[i][j]->Draw("same");

         // Horizontal lines
         centre_line->Draw("same");
         hi_line->Draw("same");
         lo_line->Draw("same");

         // Label
         label[i][j] = new TLatex();
         label[i][j]->SetNDC();
         label[i][j]->SetTextFont(43);
         label[i][j]->SetTextSize(16);
         label[i][j]->SetTextAlign(13);
         label[i][j]->DrawLatex(0.05+pad[i][j]->GetLeftMargin(), 0.97-pad[i][j]->GetTopMargin(), "#splitline{"+colLabel[i]+"}{"+rowLabel[j]+"}");
      }
   }

   // Legend
   c1->cd(0);
   TPad *leg_pad = new TPad("leg_pad","",0.0,0.0,1.0,0.63*bMargin);
   leg_pad->Draw();
   leg_pad->cd();
   TLegend *legend = new TLegend(0.35, 0.1, 0.8, 0.90);
   legend->AddEntry(h_psue[0][0],   "PS/UE", "f");
   legend->AddEntry(h_model[0][0], "NLO-PS", "f");
   legend->AddEntry(h_scale[0][0],  "Scale", "f");
   legend->AddEntry(fit[0][0],        "Fit", "l");
   legend->SetNColumns(2);
   legend->SetFillColor(0);
   legend->SetBorderSize(0);
   legend->SetTextSize(0.3);
   legend->Draw("same");

   c1->SaveAs("ww_"+commonName+".pdf");
}

TGraphErrors* ConvertHistToBand(TH1D *hist, Float_t minX, Float_t maxX)
{
   TGraphErrors *result = new TGraphErrors();
   Int_t nBins = hist->GetNbinsX();
   Int_t iPoint = 0;
   for (Int_t i=1; i<nBins+1; i++) {
      Float_t x = hist->GetBinCenter(i);
      if (x > minX && x < maxX) {
         result->SetPoint(iPoint, x, 1.0);
         result->SetPointError(iPoint, 0.0, fabs(hist->GetBinContent(i) - 1.0));
         iPoint++;
      }
   }

   return result;
}


void CanvasPartition(TCanvas *C,const Int_t Nx = 2,const Int_t Ny = 2,
                     Float_t lMargin = 0.15, Float_t rMargin = 0.05,
                     Float_t bMargin = 0.15, Float_t tMargin = 0.05)
{
   if (!C) return;

   // Setup Pad layout:
   Float_t vSpacing = 0.0;
   Float_t vStep  = (1.- bMargin - tMargin - (Ny-1) * vSpacing) / Ny;

   Float_t hSpacing = 0.0;
   Float_t hStep  = (1.- lMargin - rMargin - (Nx-1) * hSpacing) / Nx;

   Float_t vposd,vposu,vmard,vmaru,vfactor;
   Float_t hposl,hposr,hmarl,hmarr,hfactor;

   for (Int_t i=0;i<Nx;i++) {

      if (i==0) {
         hposl = 0.0;
         hposr = lMargin + hStep;
         hfactor = hposr-hposl;
         hmarl = lMargin / hfactor;
         hmarr = 0.0;
      } else if (i == Nx-1) {
         hposl = hposr + hSpacing;
         hposr = hposl + hStep + rMargin;
         hfactor = hposr-hposl;
         hmarl = 0.0;
         hmarr = rMargin / (hposr-hposl);
      } else {
         hposl = hposr + hSpacing;
         hposr = hposl + hStep;
         hfactor = hposr-hposl;
         hmarl = 0.0;
         hmarr = 0.0;
      }

      for (Int_t j=0;j<Ny;j++) {

         if (j==0) {
            vposd = 0.0;
            vposu = bMargin + vStep;
            vfactor = vposu-vposd;
            vmard = bMargin / vfactor;
            vmaru = 0.0;
         } else if (j == Ny-1) {
            vposd = vposu + vSpacing;
            vposu = vposd + vStep + tMargin;
            vfactor = vposu-vposd;
            vmard = 0.0;
            vmaru = tMargin / (vposu-vposd);
         } else {
            vposd = vposu + vSpacing;
            vposu = vposd + vStep;
            vfactor = vposu-vposd;
            vmard = 0.0;
            vmaru = 0.0;
         }

         C->cd(0);

         char name[16];
         sprintf(name,"pad_%i_%i",i,j);
         TPad *pad = (TPad*) gROOT->FindObject(name);
         if (pad) delete pad;
         pad = new TPad(name,"",hposl,vposd,hposr,vposu);
         pad->SetLeftMargin(hmarl);
         pad->SetRightMargin(hmarr);
         pad->SetBottomMargin(vmard);
         pad->SetTopMargin(vmaru);

         pad->SetFrameBorderMode(0);
         pad->SetBorderMode(0);
         pad->SetBorderSize(0);

         pad->Draw();
      }
   }
}
