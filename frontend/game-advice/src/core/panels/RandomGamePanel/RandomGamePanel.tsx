import React from "react";
import Panel from "@vkontakte/vkui/dist/components/Panel/Panel";
import PanelHeader from "@vkontakte/vkui/dist/components/PanelHeader/PanelHeader";
import Group from "@vkontakte/vkui/dist/components/Group/Group";
import { Cell } from "@vkontakte/vkui";
import { AppPanelsIds } from "..";

export const RandomGamePanel: React.FC = () => (
  <Panel id={AppPanelsIds.RandomGame}>
    <PanelHeader>Случайная игра</PanelHeader>

    <Group title="Navigation Example">
      <Cell>получить случайнукю игру</Cell>
    </Group>
  </Panel>
);
